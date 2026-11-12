# Síntese de pesquisa: método de estudo de cavaquinho

**Status:** síntese das fontes concluída; decisões e testes do aluno pendentes  
**Escopo:** aprendizagem musical, prática de acordes, contexto brasileiro e apoio visual/sonoro. Esta pesquisa não valida individualmente as 28 posições candidatas.

## Resultado executivo

As fontes apoiam um método que conecte diagramas, prática no instrumento, escuta, progressões e repertório, em vez de apresentar apenas uma tabela de acordes. Elas não determinam quais acordes são mais fáceis para este aluno, qual intervalo de revisão é ideal para ele, nem qual sequência deve ser aprovada. Essas escolhas dependem de confirmação musical e teste no cavaquinho.

## 1. Memória, revisão e aprendizagem motora

- Em um estudo com iniciantes ao piano, intervalos de 0 a 15 minutos entre sessões não produziram vantagem detectável na retenção de uma sequência motora de notas ou de trechos de canções, medidos após cinco minutos. O estudo não testou intervalos entre dias. Portanto, ele não prova que revisão espaçada seja inútil para acordes ou para sessões em dias diferentes. ([Wiseheart, D’Souza e Chae, 2017](https://doi.org/10.1371/journal.pone.0182986); `sources/memory-01-piano-spacing.md`, resumo e resultados.)
- Um estudo posterior de memória melódica encontrou melhor recordação após prática distribuída do que após prática concentrada, com teste três semanas depois. Não encontrou diferença entre intervalos de dois dias e uma semana. Os participantes aprenderam uma melodia cantada; isso não testa digitações nem trocas de acordes no cavaquinho. ([Katz e Wiseheart, 2025](https://doi.org/10.1177/03057356251401906); `sources/memory-03-melodic-spacing-2025.md`, resumo e conclusão.)
- Esses resultados não justificam prometer uma velocidade de aprendizagem ou impor um calendário “ótimo”. É razoável planejar revisões em sessões posteriores e observar se ajudam este aluno, sem apresentar esse intervalo como comprovado para o cavaquinho.
- Para o estudo de acordes, recuperar a cifra a partir da posição e a posição a partir da cifra é uma proposta prática coerente com o objetivo do projeto. As fontes reunidas não comparam diretamente esse exercício com outras formas de treino de acordes; tratá-lo como uma escolha de projeto a avaliar, não como resultado provado.

## 2. Sequência de estudo e aplicação musical

- A análise de métodos brasileiros de cavaquinho identifica limitações em materiais organizados como dicionários de acordes e recomenda contextualizar acordes com progressões, instruções de troca e levadas. O autor propõe combinar notação, indicações da palhetada e exemplos em áudio para explicar ritmos. É uma análise metodológica com propostas do autor, não um ensaio que compare sequências para iniciantes. ([Croset Junior, UNIRIO, 2020](https://www.unirio.br/cla/ivl/cursos/luizcroset.pdf); `sources/sequence-01-unirio-cavaquinho-methods.md`, seções 3.1–3.4 e considerações finais.)
- O programa de prática de cavaquinho do IFCE integra repertório progressivo, percepção auditiva, acompanhamento, harmonia, técnica e palhetada. Isso mostra uma abordagem institucional integrada; não define a ordem ideal para este aluno. ([IFCE, Prática de Instrumento Específico I](https://portal.ifce.edu.br/documents/14468/MUS007_-_Pr%C3%A1tica_de_Instrumento_Espec%C3%ADfico_I_Cavaquinho.pdf); `sources/sequence-02-ifce-cavaquinho-i-syllabus.md`, ementa, objetivos e programa.)
- A pesquisa qualitativa da UFMG sobre quatro músicos populares registra práticas como ouvir e copiar, tocar de ouvido, experimentar e aprender em interação com outras pessoas. O número e o perfil dos participantes não permitem afirmar que essas práticas sejam superiores para todos; são razões para respeitar repertório, experiência e batida já conhecidos pelo aluno. ([Coelho, UFMG, 2016](https://repositorio.ufmg.br/server/api/core/bitstreams/162c391f-c5d8-47d6-81cf-087fe808e9a1/content); `sources/sequence-03-ufmg-informal-learning.md`, capítulos 5 e 6.)
- Aplicação ao projeto: depois de confirmar a base, estudar poucos acordes aprovados, praticar reconhecimento e som, ligar trocas e só então contextualizá-los em uma progressão e em repertório compatível. O quadradinho G–E7–Am–D7 continua sendo apenas candidato; nenhuma dessas fontes comprova que seja o mais fácil.

## 3. Diagramas, som e recursos digitais

- Os materiais de cavaquinho analisados usam informações visuais como nomes das cordas, casas, dedos e notas. Para evitar ambiguidade, o projeto deve manter a afinação de referência visível, identificar primeira e quarta cordas, numerar casas e descrever corda/casa/dedo em texto. Uma imagem publicada documenta uma forma naquele material, mas não demonstra que seja fácil ou adequada para este aluno. (`sources/sequence-01-unirio-cavaquinho-methods.md`, análise dos diagramas; ver também `aprendizado_cavaquinho/04_PESQUISA_E_REFERENCIAS.txt`.)
- Em um estudo com 115 estudantes de violão e piano, tocar com som, ouvir a peça e praticar sem som tiveram efeitos diferentes. A prática tocando e ouvindo esteve associada a menos erros de entonação; ouvir sem tocar favoreceu aspectos de articulação e fluidez; praticar sem som favoreceu estrutura rítmica e fluidez. Os autores observaram maior relevância do feedback auditivo para iniciantes. Isso apoia combinar imagem e som como recursos complementares, mas não prova que um áudio específico ensine cavaquinho nem que o aplicativo consiga avaliar a execução. ([Luciani, Cortelazzo e Proverbio, 2022](https://doi.org/10.1038/s41598-022-24262-x); `sources/memory-02-auditory-feedback.md`, resumo e resultados.)
- A documentação MDN descreve a Web Audio API, que é uma API de navegador. Ela não é uma receita para implementar áudio em PySide. A especificação W3C de acessibilidade consultada trata de SVG e mapeamentos de acessibilidade; não especifica como tornar um `QPainter` acessível. São referências de contexto, não justificativa para adicionar dependências web ou prometer acessibilidade do widget atual. (`sources/visual-audio-03-mdn-web-audio.md`; `sources/visual-audio-04-w3c-svg-aam.md`.)
- O guia de cavaquinho de Portugal descreve sobretudo o instrumento minhoto e afinações portuguesas. Não deve ser usado para validar a afinação Ré–Sol–Si–Ré ou as posições do cavaquinho brasileiro deste projeto. (`sources/visual-audio-05-tradmusic-cavaquinho.md`.)

## Recomendações para o projeto

1. Não mostrar as 28 posições como conteúdo aprovado. Validar convenções, desenhos e afinação antes de escolher as formas iniciais.
2. Apresentar poucos acordes por etapa, com diagrama acompanhado de instrução em texto e identificação explícita das cordas.
3. Incluir recuperação ativa nos dois sentidos como hipótese de exercício: nome/cifra → posição e posição → nome/cifra. Reavaliar com o aluno.
4. Depois de validar as formas, praticar acordes isolados, trocas em andamento confortável e aplicação em uma progressão cuja função harmônica tenha sido conferida.
5. Para levadas, combinar demonstração visual com indicação de palhetada e, se houver gravação validada, exemplo sonoro. O material não deve ensinar novamente a batida básica que o aluno já conhece.
6. Retomar os acordes em sessões posteriores, sem fixar um intervalo ideal ou prometer rapidez. Acompanhar se o aluno reconhece a forma, toca limpo e troca no pulso.
7. Não há evidência nestas fontes de que IA seja necessária. Os exercícios de reconhecimento e as trocas podem começar com regras explícitas e conteúdo validado. Avaliação automática pelo microfone exigiria pesquisa técnica e validação próprias.

## Limites e pendências que a pesquisa não resolve

- Confirmar com o aluno a afinação real e os sentidos de “sustenida” e “com sétima”.
- Conferir as posições candidatas em fontes brasileiras independentes e testar som, conforto e trocas no instrumento.
- Receber as imagens de Am mencionadas pelo aluno antes de comparar as digitações.
- Escolher acordes iniciais, quadradinho, duas levadas e repertório somente depois das validações anteriores.
- Nenhuma fonte estabelece quais formas são mais fáceis para a mão deste aluno.
- Os estudos de memória e feedback envolvem melodia, piano ou violão; não testam a sequência pedagógica deste aplicativo nem o cavaquinho brasileiro.
- As fontes de busca em `sources/memory-snippets.md` são apenas trechos de resultados, não textos completos; não foram usadas como evidência principal. `sources/visual-audio-01-unirio-cavaco-methods.md` e `sources/visual-audio-02-auditory-feedback-study.md` duplicam fontes já arquivadas e não contam como estudos independentes.

## Checklist da pergunta de pesquisa

- [x] Dividir em poucos acordes aprovados por etapa e revisá-los em sessões posteriores, sem afirmar intervalo ideal.
- [x] Propor recuperação de cifra/nome e posição nos dois sentidos, explicitando que ainda deve ser avaliada com o aluno.
- [x] Introduzir progressões e músicas depois de validar os acordes, sem declarar o candidato atual como definitivo.
- [x] Tornar afinação, orientação, cordas, casas e dedos explícitos em cada diagrama.
- [x] Tratar áudio e prática tocada como complemento; as fontes não demonstram superioridade universal sobre imagens ou texto.
- [x] Começar com exercícios determinísticos; as fontes não justificam IA nem análise automática por microfone.
- [x] Separar decisões que só o aluno pode confirmar e resultados que exigem teste no instrumento.

## Fontes principais

- Wiseheart, D’Souza e Chae (2017), estudo de espaçamento em aprendizagem de piano: `sources/memory-01-piano-spacing.md`.
- Katz e Wiseheart (2025), aprendizagem espaçada e memória melódica: `sources/memory-03-melodic-spacing-2025.md`.
- Luciani, Cortelazzo e Proverbio (2022), feedback auditivo em estudantes de piano e violão: `sources/memory-02-auditory-feedback.md`.
- Croset Junior (2020), análise de métodos brasileiros de cavaquinho: `sources/sequence-01-unirio-cavaquinho-methods.md`.
- IFCE, programa da disciplina de cavaquinho: `sources/sequence-02-ifce-cavaquinho-i-syllabus.md`.
- Coelho (2016), práticas informais de quatro músicos populares: `sources/sequence-03-ufmg-informal-learning.md`.
