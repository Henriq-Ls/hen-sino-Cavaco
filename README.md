# hen-sino-Cavaco

Aplicativo desktop em PySide6 para organizar um método de estudo passo a passo
de cavaquinho brasileiro, com foco inicial em samba e pagode. A proposta é
orientar o que praticar; o aplicativo não é um professor virtual.

## Estado atual

O protótipo inclui:

- Janela principal com páginas Início, Trilha e Acordes.
- O aplicativo abre diretamente na página de acordes.
- Trilha estática com seis etapas planejadas.
- Matriz visual 7 × 4 com 28 posições candidatas calculadas.
- Diagrama selecionável com cifra, afinação, casas, dedos e notas por corda.
- Preferências de tema salvas localmente e restauração da geometria da janela.

As 28 posições ainda não foram confirmadas individualmente em fontes
independentes nem testadas no instrumento. A afinação mostrada é a referência
Ré–Sol–Si–Ré; os sentidos de “sustenida” e “com sétima” continuam provisórios.
O aplicativo não registra progresso nem tem exercícios interativos, avaliação
de trocas, áudio, metrônomo ou análise pelo microfone. Consulte
`nucleo/_DOC_STATUS.txt` para o estado atualizado e `research/notes.md` para a
síntese das fontes pedagógicas.

## Executar

Instale as dependências dentro desta pasta:

```sh
python -m pip install -r requirements.txt
python main.py
```

`qtawesome` é opcional; os ícones de configurações têm alternativas Qt.
O ponto de entrada e a janela foram verificados em modo offscreen; não há
workflow configurado para prévia visual.

## Documentos do projeto

- `nucleo/_DOC_PROJETO.txt` — objetivo, estrutura e decisões de arquitetura.
- `nucleo/_DOC_STATUS.txt` — implementação atual e pendências.
- `BASE_DO_PROJETO.txt` — base pedagógica e decisões musicais pendentes.
- `aprendizado_cavaquinho/` — currículo, validações e matriz candidata.
- `research/` — síntese e fontes preservadas.
