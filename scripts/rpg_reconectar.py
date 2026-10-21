#!/usr/bin/env python3
"""Inicia o OpenCode e pausa quando a autenticação do Discord deixa de funcionar.

A chave é lida do ambiente ou digitada sem eco e NÃO é gravada em arquivos.
Este programa NÃO extrai, renova ou prevê tokens do Discord.
"""

import getpass
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
from pathlib import Path

API = "https://discord.com/api/v10/users/@me"
INTERVALO = 120  # segundos entre verificações; não usa créditos do GPT
TOKEN_VALIDO = re.compile(r"^[A-Za-z0-9._-]+$")


def verificar(token):
    """Consulta a API com curl, enviando a credencial pela entrada padrão."""
    if not TOKEN_VALIDO.fullmatch(token):
        return "formato"
    # --config - evita pôr a chave nos argumentos visíveis de processos.
    parametros = f'header = "Authorization: {token}"\n'
    try:
        result = subprocess.run(
            ["curl", "--silent", "--show-error", "--max-time", "15",
             "--output", "/dev/null", "--write-out", "%{http_code}",
             "--config", "-", API],
            input=parametros, capture_output=True, text=True, timeout=20,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "rede"
    if result.returncode:
        return "rede"
    return result.stdout.strip()


def ler_chave():
    try:
        return getpass.getpass("Cole a chave atual do Discord (oculta): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrado.")
        return None


def escolher_token(token):
    while True:
        if not token:
            token = ler_chave()
            if not token:
                return None
        estado = verificar(token)
        if estado == "200":
            print("✅ Autenticação aceita (HTTP 200).", flush=True)
            return token
        if estado == "401":
            print("⚠️  HTTP 401: credencial recusada. Precisa de outra chave.")
            token = None
            continue
        if estado == "formato":
            print("⚠️  Formato inesperado. Não inclua aspas ou espaços.")
            token = None
            continue
        print(f"⚠️  Verificação inconclusiva ({estado}). Nenhuma mensagem foi enviada.")
        try:
            resposta = input("[t] tentar de novo, [n] nova chave, [s] sair: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return None
        if resposta == "n":
            token = None
        elif resposta != "t":
            return None


def vigiar(token, parar, eventos):
    while not parar.wait(INTERVALO):
        estado = verificar(token)
        if estado in ("401", "403"):
            eventos.put(estado)
            return
        if estado != "200":
            print(f"\n⚠️  Verificação temporariamente indisponível ({estado}); aguardando.", flush=True)


def encerrar_processo(processo):
    if processo.poll() is not None:
        return
    processo.terminate()
    try:
        processo.wait(timeout=8)
    except subprocess.TimeoutExpired:
        processo.kill()
        processo.wait(timeout=5)


def iniciar():
    if not shutil.which("curl") or not shutil.which("opencode"):
        print("Instale curl e OpenCode antes de usar este script.")
        return 1
    projeto = Path(__file__).resolve().parent.parent
    token = os.environ.get("DISCORD_TOKEN", "").strip() or None
    while True:
        token = escolher_token(token)
        if token is None:
            return 0
        ambiente = os.environ.copy()
        ambiente["DISCORD_TOKEN"] = token
        print("🚀 Abrindo OpenCode. O histórico do RPG permanece nos arquivos do projeto.", flush=True)
        try:
            processo = subprocess.Popen(["opencode"], cwd=projeto, env=ambiente)
        except OSError as erro:
            print(f"Não foi possível abrir o OpenCode: {erro}")
            return 1
        parar = threading.Event()
        eventos = queue.Queue()
        vigia = threading.Thread(target=vigiar, args=(token, parar, eventos), daemon=True)
        vigia.start()
        falha = None
        try:
            while processo.poll() is None:
                try:
                    falha = eventos.get(timeout=1)
                    break
                except queue.Empty:
                    pass
        except KeyboardInterrupt:
            print("\nEncerrando OpenCode...")
            encerrar_processo(processo)
        finally:
            parar.set()
            vigia.join(timeout=1)
        if falha:
            print(f"\n🛑 Discord retornou HTTP {falha}. Pausando o OpenCode para evitar ações repetidas.", flush=True)
            encerrar_processo(processo)
            if falha == "401":
                token = None  # pedir nova chave; nunca tentar extraí-la do navegador
                continue
            try:
                resposta = input("[t] verificar novamente, [n] nova chave, [s] sair: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                return 0
            if resposta == "t":
                continue
            if resposta == "n":
                token = None
                continue
        return processo.returncode or 0


if __name__ == "__main__":
    sys.exit(iniciar())
