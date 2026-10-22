# Sistemas — Naruto Full Power

Conferência em 21/10/2026 pelo MCP `discord-rpg`. Servidor `744274389570420776`. Este documento complementa [HISTORICO_FULL_POWER.md](HISTORICO_FULL_POWER.md).

## Estado de cobertura

**Em andamento, não é leitura integral de todo o servidor.** Cada consulta usa uma janela recente de até 200 mensagens, sem cursor de paginação. Resposta vazia e timeout não equivalem a regra inexistente. Imagens, tópicos e links externos não estão todos auditados. Os anexos ilustrativos não foram baixados em massa.

As consultas desta continuação foram feitas individualmente. Os timeouts anteriores não impediram recuperar missões, batalhas, vilas e habilidades na nova rodada expressamente pedida pelo jogador.

## Novas fontes consultadas

Limite 200 em cada canal abaixo.

| Canal | ID | Resultado |
|---|---|---|
| Missões | 873208529517953044 | Texto recuperado; 1559602059437678594–1559605742909001851 |
| Batalhas | 856852805205622794 | Texto recuperado; 1487848376916770906–1487848835085500476 |
| Vilas | 793118258072125450 | Texto recuperado; 1493346908435910727–1493350802205704263 |
| Habilidades | 840928936145977344 | Texto recuperado; 1501357519048802365–1501361154176319558 |
| Info-jutsu | 1009439273847619604 | Retorno vazio |
| Economia | 958027927101009940 | Timeout |
| Força | 1155979979679604747 | Texto recuperado; 1491503489275138199–1491504903594578000 |
| Info-habilidades | 1009441863259914270 | Retorno vazio |
| Info-vilas | 857370776223219772 | Texto recuperado; 1493351641217241210–1493354262837858334 |
| Info-comércio | 903373008285093949 | Retorno vazio |
| NPCs | 1018925120414306384 | Timeout |
| Compras | 1009498407880114256 | Janela recente recuperada, termina em 1425606642367463577; transações antigas de terceiros e anúncio de loja fechada. Não prova tabela comercial atual |
| Equipamentos | 1196959299356868778 | Texto recuperado; 1441791538236620940–1445601230050169034 |
| Shinobi | 789505496742101004 | Texto recuperado; 1504640389104009257–1504643037341552790 |
| Equipes | 929432097150619678 | Texto recuperado; 1333940199788511285–1460020530794201141; inclui versões antigas e novas |
| Aptidão | 789280032601407488 | Ampliado de 40 para 200; 1501567672918212734–1501569729771339859 |
| Timeskip | 1487477097088946266 | Texto recuperado; 1529908392250835165–1555159962072907797 |
| Lore | 1158795716001542305 | Texto recuperado; 1510529663942918294–1556451621645455431 |

As leituras de status, chakra, aprendizagem, elementos, prodígio, level-boost e outros constam do histórico do personagem. Esta tabela não substitui aquele registro nem conta consultas anteriores como novas.

## Missões

Fontes principais: solicitação `1559602238140448772`, rank D `1559602444638617681`, observações `1559602912500650079`.

- Solicitar no escritório do kage. O sistema permite iniciar o deslocamento sem marcar o kage nem aguardar sua resposta.
- Fazer o choose correspondente ao rank; não escolher por conveniência o resultado aleatório.
- Limite: 3 missões por dia, até 4 participantes por missão.
- Não roubar itens, corpos, olhos ou sangue dos NPCs. Não os controlar para reutilizar em outras missões.
- Missões não podem sofrer intervenção para ajudar ou atrapalhar. Depois de finalizadas, 15 minutos de proteção para sair.

| Rank | Requisitos e execução | Recompensa após concluir | Cooldown para outra missão |
|---|---|---|---|
| D | Qualquer ninja; `+choose Limpeza, Busca por Animaizinhos, Transporte de Mercadorias` | 25.000 all; `+roll 5000..30000` em ryos | 1 hora |
| C | Qualquer ninja; choose Escolta/Captura/Resgate/Espionagem. Pode autonarrar com 1.000 caracteres totais, +500 por participante extra | 50.000 all; `+roll 30000..100000` | 2 horas |
| B | Jounin/chuunin solo; genin em dupla ou mais. Autonarração: 2.000 caracteres, +500 por extra | 100.000 all; `+roll 80000..160000` | 3 horas |
| A | Jounin solo, chuunin em dupla, genin em trio. Autonarração: 3.000 caracteres, +1.000 por extra | 150.000 all; `+roll 150000..200000` | 4 horas |
| S | Narrador obrigatório; jounin solo, chuunin em trio, genin não pode | 200.000 all; `+roll 250000..400000` | 6 horas |

Para B/A/S o choose inclui Massacre além das quatro opções de C. As configurações de inimigos narrados constam nas mensagens de cada rank: C `1559602526725214358`, B `1559602621118156890`, A `1559602719231180810`, S `1559602822419321013`. Conferir esses valores antes de uma missão com narrador.

### Rank D: execução exata

- Limpeza: ação de faxina num canal da vila ou do país e lembrete de 10 minutos.
- Busca por Animaizinhos: ação capturando sem ferir, lembrete de 20 minutos e levar ao cliente no gabinete ao terminar.
- Transporte de Mercadorias: buscar num canal do país, ação e lembrete de 30 minutos, depois levar a um canal da vila.
- Respeitar o sistema de locomoção em cada trajeto. Nenhuma dessas missões foi iniciada nesta conferência.

## Batalhas

- Combates podem ser por ações ou comandos. Em desacordo, choose define o formato.
- Iniciativa: cada um usa `+Roll 10`; o maior começa. Em empate, quem rolou depois repete.
- Turno individual permite ativações, defesa/esquiva e ataque/contra-ataque. Em comandos, técnica ofensiva encerra o turno.
- Rodada é o conjunto dos turnos de todos.
- Colisão: vence o maior dano; igualdade anula. Taijutsu/kenjutsu iguais podem levar a embate de forças solicitado por um lado: `+roll 15`, vencedor acerta com 50% do dano original.
- Alcance: curto 0–5 m; médio 5–10 m; longo acima de 10 m. Não ampliar sem regra da técnica.
- Reação padrão: 1,5x a velocidade.
- Não decidir detalhes da ação alheia; perguntar quando faltar especificação. Preferir escrita clara e objetiva.
- Em comando que diga hitkill em ponto vital, atacante usa `+choose Vital, Não Vital`, salvo choose próprio da técnica.

## Vilas e coerência da primeira cena

- Kumo é do País do Relâmpago, em montanhas altas, escondida nas nuvens.
- Info-vilas permite ao ninja começar normalmente na vila escolhida na ficha. A primeira cena de Henrique dentro da entrada de Kumo é compatível com essa regra.
- Para outra vila não aliada, pode haver guarda chuunin barrando e necessidade de narrador. Não presumir livre trânsito.
- Renegados precisam de narração obrigatória dos guardas para invasão, salvo entrada via ninjutsu espaço-tempo.
- Ação passando pela entrada é normalmente obrigatória, exceto na própria aldeia; essa exceção não vale para renegado invadindo sua antiga aldeia.
- Cadastro de Vilas exibe líderes como pontos e habitantes 0/30, mas a registradora informou Konoha lotada e confirmou Kumo. Não usar o cadastro genérico para desfazer a decisão atual da registradora.
- Invasão/destruição/roubo de pergaminho: cooldown de 7 dias para vila; pessoa/grupo espera 3 dias para outro alvo, respeitando o anterior. Limites: 4 invasores e 6 defensores players.

## Habilidades: efeitos e obtenção

Ter uma regra de obtenção não significa possuir a habilidade. São caminhos futuros, salvo benefício de clã confirmado.

| Habilidade | Regra lida |
|---|---|
| Vigor Elevado | +100.000 vitalidade; reduz pela metade efeitos temporários de redução de físicos. Shimura confere a habilidade; verificar se a registradora já contabilizou antes de somar |
| Resistência Aprimorada | 20% menos dano recebido ou de ativação que consuma vida; nível 20 e treino de 3h/dia por 3 dias |
| Ambidestria | Roll próprio 90+; ou nível 20, 2h/dia por 3 dias e roll 70+ |
| Flexibilidade Elevada | +95.000 velocidade em movimentos de flexibilidade; nível 20 e 2h/dia por 3 dias |
| Selos em Alta Velocidade | Nível 30 e 3h/dia por 3 dias |
| Armazém Interno | Nível 30, 3h/dia por 3 dias, roll único 80+ |
| Adaptação Combativa | Enfrentar força/velocidade superior por 4 turnos; adaptação leva 2 turnos, até 300.000 velocidade e um nível de força acima |
| Persistência em Combate | Resistência Aprimorada e combate real com inimigo em que vitalidade chegue a 30% |
| Memória Eidética | Roll na ficha; texto diz `+95` |
| Intelecto Avançado | Prodígio e roll 95+; ou sorteios/eventos |
| Atos Reflexos | Dois desvios garantidos por combate; obtenção por eventos/sorteios no texto geral |
| Reação Superior | Acrescenta 1,5x na reação; eventos/sorteios |

Também lidos: manuseio de venenos, confecção de armadilhas, alta precisão, furtividade, audição extrema, regeneração, conversa com animais, intenção assassina, manipulação de fios, personificação de chakra, corpo compatível e imunidade a venenos. Não há comprovação de posse por Henrique.

## Força

Evolução exige sempre o patamar anterior. Bônus de dano se aplicam a bukijutsu/taijutsu/kenjutsu quando dependem de braços/pernas.

| Patamar | Obtenção natural | Levantamento comum | Dano adicional |
|---|---|---:|---:|
| Normal | Inicial | 45 kg | Nenhum |
| Anormal | Treino 2h | 120 kg | 30.000 |
| Absurda | 2h/dia por 3 dias | 200 kg | 100.000 |
| Descomunal | 4h/dia por 4 dias | 300 kg | 150.000 |
| Extraordinária | Descomunal, nível 40, 2h/dia por 4 dias e roll 70+ | 1.000 kg | 200.000 |

Nenhum treino de força pessoal foi realizado ou creditado nesta consulta.

## Equipamentos

- Kunai e shuriken podem ser recebidas por aptidão em bukijutsu; espada por kenjutsu. Quantidades pessoais precisam ser conferidas no sistema de aptidões/inventário.
- Kit básico: 10 kunai, 10 shuriken, 5 amuletos explosivos, 3 fios de aço. Não presumir que Henrique o recebeu.
- Lâmina de Chakra criada: nível 30, kenjutsu/bukijutsu e pagamento de 1 milhão de ryos ao UnbelievaBoat.
- Ferramentas especiais, itens de clã, armas lendárias e contratos têm requisitos próprios. Texto geral não autoriza criar posse narrativa.
- O canal contém nota antiga “atualizar”; confirmar divergências atuais com a equipe.

## Aptidões: confirmação ampliada

- Bukijutsu confere **kit ninja básico** (`1501567955715096647`). Isso fundamenta o direito do personagem ao kit pela aptidão do clã; ainda é preciso verificar seu registro pessoal e se já foi entregue antes de criar uma segunda entrada ou somar itens.
- Bukijutsu permite roll de precisão elevada: **mais de 95**. Não executar novamente sem saber se já foi feito.
- Bunshinjutsu pode ser escolhido na ficha e dá acesso aos clones de clã/vila **desde que cumpra os requisitos**. Não significa ter Kage Bunshin ou clone físico automaticamente.
- Básicas adicionais por treino: 6 horas cada, limite de duas obtidas por esse método, solicitar cargo em Att-Cargos após término.
- Maestria: -20% custo de chakra e +10% dano/defesa da aptidão; efeitos especiais por categoria. Henrique não tem maestria comprovada.
- O texto de maestrias deixa uma lacuna entre níveis 36–39; não inventar um limite para essa faixa.

## Equipes: versões e caminho futuro

O canal contém textos antigos de `Deleted User` e uma sequência posterior de `rusk_ai` reescrevendo os mesmos esquadrões. Não combinar recompensas das duas versões. Confirmar com a staff se houver dúvida sobre vigência.

- Versão posterior da ANBU (`1446306430092312627`): nível 20 e 500.000 em todos os atributos, pedir ao kage e passar no teste prático; secretário exige nível 30, 1.000.000 all e nomeação. Exige missão B+ semanal.
- **Unidade Kinkaku** (`1460000064989823076`): shinobi de Kumo, nível 30 e bukijutsu. Pedir ao raikage; NPC exige roll 60+. Benefícios incluem ambidestria, maestria em bukijutsu e armazém interno; extras exclusivos do primeiro membro não podem ser presumidos.
- Sensorial (`1446311611391541330`): nível 20 e sensoriamento de chakra; ingresso por kage ou roll 60+ com NPC, reduzido em 20 com maestria em tansakujutsu. Exige 5 horas de vigilância por semana.
- Outras equipes lidas: Médica, Explosivos, Espadachins da Névoa, Marionetes, Corpo Suicida, Quarteto do Som, Doze Guardiões, Antiterrorista, Criptograma e Bandidos Mujina. Não atribuir participação a Henrique.
- Observações posteriores (`1460020507184205835`): máximo duas equipes, liderar uma; manter recompensas após sair exige um timeskip. Duas chances de ingresso; após duas falhas, aguardar timeskip de pelo menos três meses. Texto antigo mencionava 15 dias, portanto não aplicá-lo como se fosse a versão posterior.
- Bandidos Mujina: o próprio texto registra impossibilidade de ingresso por enquanto.

## Contexto temporal e lore

- Timeskip inclui recompensas de julho/agosto de 2026 com prazos explícitos, e termina com anúncio de **novo reset** (`1555159957773619201`). Não conceder automaticamente a Henrique skips, ganhos ou idade referentes a campanhas anteriores.
- Lore posterior ao reset (`1556428896541478963` e seguintes): tensão entre as cinco nações e presença de dragões. No País do Raio, o texto cita Nidhogg.
- Não tratar segredos descritos ao leitor como conhecimento pessoal de Henrique. Não iniciar encontro com dragão nem roll especial nesta auditoria.
- A história modesta de infância em Kumo e a primeira cena no portão não reivindicam participação em eventos anteriores nem poderes de lore.

## Pendências

- Economia e NPCs: timeout nesta rodada; não repetir em loop.
- Info-jutsu, info-habilidades e info-comércio: retorno vazio. Não há texto validado nesses canais.
- Demais sistemas especializados: registrar cada canal à medida que for consultado; a leitura global ainda não está concluída.
- Ficha pessoal: faltam confirmação dos valores de atributos/nível, imagem e inventário. Não executar rolls de criação já feitos nem contabilizar Vigor em duplicidade.
- Não houve novo envio de mensagem, edição de ficha, treino, missão, compra, roll ou alteração de cargo nesta auditoria.

### Fila especializada identificada, ainda sem leitura nesta auditoria

Esta lista é um checkpoint por nomes/IDs conhecidos, não prova de filiação exata às categorias nem inventário de todos os canais do servidor.

| Canal | ID |
|---|---|
| Técnicas especiais | 1019362745474367570 |
| Estilos de luta | 963876574032191548 |
| Métodos taijutsu | 903373889629990972 |
| Pergaminhos | 789845526861709402 |
| Invocação | 987099995108958310 |
| Medicina | 789216731036909609 |
| Biomedicina | 1358145941915303936 |
| Marionetes | 904854803006513162 |
| Chooses | 918579008789172274 |
| Criações | 1556676467306270730 |
| Títulos | 1489395518936186940 |
| Postos | 1556287030458187856 |
| Chefes e conselheiros | 792696994874916864 |
| Líder de clã | 903797970581983312 |
| Organizações | 917219071345442836 |
| Kits | 1026563800893247568 |
| Encarnações | 1301564303446511678 |
| Sharingan | 856572716889931806 |
| Mangekyou Sharingan | 1009445335967473815 |
| Byakugan | 1008839372793200731 |
| Rinnegan | 856573520028631051 |
| Tenseigan | 1078351522905194637 |
| Kekkei genkai | 789478525555965962 |
| Jinchuuriki | 848346949710118972 |
| Dominar bijuu | 1498356901677629561 |
| Árvore divina | 856254231010738247 |
| Modo sennin | 1076921677910388776 |
| Rikudou senninka | 1076948647788425307 |
| Juinka | 856907138839740458 |
| Byakugou | 856902608807919669 |
| Karma | 811922648602902618 |
| Imortalidade | 808037702963298334 |
| Espadas da Névoa | 792714537606316043 |
| Tesouros Rikudou | 814597879154081822 |
| Info-doujutsu | 856569114030374952 |
| Info-bijuu | 856910765100105728 |
| Info-senninka | 856892557815447573 |
| Info-ootsutsuki | 857343858022416394 |

A auditoria integral permanece aberta por essa fila, pelos erros registrados, pelos tópicos/anexos e pela ausência de paginação. Não usar a existência deste arquivo ou do índice no README como certificado de leitura total.
