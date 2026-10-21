#!/usr/bin/env python3
"""Inicia o OpenCode e pausa quando a autenticação do Discord deixa de funcionar.

A chave é lida do ambiente ou digitada sem eco e NÃO é gravada em arquivos.
Este programa NÃO extrai, renova ou prevê tokens do Discord.
"""

import fcntl
import getpass
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
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

def obter_bloqueio():
    """Impede duas instâncias do reconector no mesmo Codespaces."""
    pasta = Path.home() / ".cache" / "naruto-rpg-ia"
    try:
        pasta.mkdir(mode=0o700, parents=True, exist_ok=True)
        fd = os.open(str(pasta / "reconector.lock"), os.O_CREAT | os.O_RDWR, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(fd)
            print("⚠️  Já existe um reconector aberto. Use a aba daquele terminal.")
            return None
        return fd
    except OSError as erro:
        print(f"Não foi possível iniciar o reconector: {erro}")
        return None


def perguntar(texto):
    try:
        return input(texto).strip().lower()
    except (EOFError, KeyboardInterrupt):
        return "s"


def iniciar():
    if not shutil.which("curl") or not shutil.which("opencode"):
        print("Instale curl e OpenCode antes de usar este script.")
        return 1
    projeto = Path(__file__).resolve().parent.parent
    token = os.environ.get("DISCORD_TOKEN", "").strip() or None
    falhas_seguidas = 0
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
            return 0
        finally:
            parar.set()
            vigia.join(timeout=1)
        if falha:
            falhas_seguidas = 0
            print(f"\n🛑 Discord retornou HTTP {falha}. Pausando o OpenCode para evitar ações repetidas.", flush=True)
            encerrar_processo(processo)
            if falha == "401":
                token = None  # pedir nova chave; nunca tentar extraí-la do navegador
                continue
            resposta = perguntar("[t] verificar novamente, [n] nova chave, [s] sair: ")
            if resposta == "t":
                continue
            if resposta == "n":
                token = None
                continue
            return 0

        codigo = processo.returncode
        if codigo == 0:
            falhas_seguidas = 0
            print("\nℹ️  O OpenCode foi fechado, mas o reconector continua aberto.")
            print("Não precisa informar a chave outra vez se ela ainda estiver válida.")
            if perguntar("[r] reabrir OpenCode, [s] sair: ") == "r":
                continue
            return 0

        falhas_seguidas += 1
        print(f"\n⚠️  OpenCode encerrou com código {codigo}.", flush=True)
        if falhas_seguidas <= 2:
            print("Tentando abrir novamente em 3 segundos...", flush=True)
            time.sleep(3)
            continue
        print("O OpenCode falhou 3 vezes. Parei para não criar um ciclo infinito.")
        falhas_seguidas = 0
        if perguntar("[r] tentar novamente, [s] sair: ") == "r":
            continue
        return codigo or 1


def main():
    bloqueio = obter_bloqueio()
    if bloqueio is None:
        return 2
    try:
        return iniciar()
    finally:
        os.close(bloqueio)


if __name__ == "__main__":
    sys.exit(main())
