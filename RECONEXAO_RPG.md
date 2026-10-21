# Reconector do RPG (OpenCode + Discord MCP)

Este script mantém uma sessão do **OpenCode** e verifica a autenticação do Discord
a cada 120 segundos sem usar créditos do modelo de IA.

## Como usar no GitHub Codespaces

1. Feche outras sessões do OpenCode para não deixar instâncias antigas usando a credencial anterior.
2. Abra um terminal Bash dentro do Codespaces.
3. Execute:

```bash
cd /workspaces/naruto-rpg-ia
git pull
python3 scripts/rpg_reconectar.py
```

4. Se não houver `DISCORD_TOKEN` no ambiente, o programa pedirá a chave no próprio terminal sem exibi-la.
5. Se a autenticação for aceita (HTTP 200), ele abrirá o OpenCode no diretório do projeto.

## O que acontece se a conexão falhar?

- **401:** o OpenCode é interrompido, o script solicita uma nova chave e verifica a autenticação antes de reabri-lo.
- **403:** o OpenCode é interrompido e o script oferece repetir a verificação, informar outra chave ou sair. Isso não prova que o token está inválido.
- **Falha de rede ou 429:** aparece um aviso, e o script volta a verificar na próxima rodada, sem insistir rapidamente.
- **OpenCode fechado normalmente:** o reconector continua aberto e oferece `[r] reabrir OpenCode` ou `[s] sair`. A chave permanece só na memória enquanto o reconector estiver aberto.
- **OpenCode fecha com erro:** o reconector tenta reiniciar até duas vezes, com pequena pausa; após três falhas, pede uma escolha para evitar um ciclo infinito.
- **Duas instâncias:** um bloqueio impede iniciar dois reconectores ao mesmo tempo no mesmo Codespaces.

Isso **não captura tokens automaticamente** nem prevê a sua troca. A verificação HTTP
testa a autenticação na API, mas não garante que o gateway Discord esteja pronto.

## Segurança e limites

- O token é mantido apenas na memória do processo e herdado pela sessão do OpenCode.
- O token não é escrito no repositório, em arquivo .env ou nos logs pelo script.
- Não envie tokens em prints, chats, commits ou comandos de terminal visíveis.
- O script **não envia mensagens** ao Discord; só gerencia a sessão local do OpenCode.
- Sua sessão RPG continua nos arquivos do Codespaces, como `HISTORICO_RPG.md`, se o arquivo existir. Este script não o modifica.
- O monitor para quando o Codespaces é encerrado/suspenso; não é um serviço 24 horas.
- O supervisor não executa jogadas sozinho: quem lê e age é a sessão do OpenCode, quando houver uma tarefa ativa.
- A verificação da API não demonstra que a conexão do gateway do Discord esteja pronta; confirma apenas a resposta HTTP à autenticação.
- Automação de contas pessoais do Discord ("self-bots") pode violar as regras da plataforma.

## Sem precisar usar OpenCode nem gastar cota

O supervisor confere o status da autenticação por HTTP diretamente no terminal; isso não
utiliza um modelo de IA. Uso do OpenCode com GPT, no entanto, continua consumindo a cota
aplicável ao plano.

## Diagnóstico rápido pelo celular

Se a tela voltar ao Bash (`$`), o OpenCode encerrou. Nas versões atuais do
reconector, escolha `r` na pergunta `[r] reabrir OpenCode, [s] sair`.
Se você já saiu completamente do programa, rode novamente `python3 scripts/rpg_reconectar.py`.
Se o Código Python falhar ao iniciar depois de um `git pull`, verifique a sintaxe com
`python3 -m py_compile scripts/rpg_reconectar.py`. Esse teste não chama o Discord.
