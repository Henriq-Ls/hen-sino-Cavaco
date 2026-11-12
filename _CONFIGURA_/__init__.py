# _CONFIGURA_/__init__.py
"""
Fonte única de verdade para TODOS os valores fixos do projeto.
Nenhum outro arquivo pode ter cores, atalhos, tamanhos ou qualquer
valor fixo — tudo vem daqui.

SEÇÕES:
    APPDATA
    APLICAÇÃO
    FONTES
    JANELA PRINCIPAL
    ATALHOS
    CORES — paleta base
    CORES — UI escuro
    ESTILOS QSS prontos
"""

import os
import re

# ══════════════════════════════════════════════════════════════════════════════
# MODO DE EXECUÇÃO
# ══════════════════════════════════════════════════════════════════════════════
# True  → desenvolvimento: log em nível DEBUG, erros detalhados
# False → produção: log em nível ERROR apenas, sem stack traces no terminal
MODO_DEV = True

# ══════════════════════════════════════════════════════════════════════════════
# APPDATA — pasta do usuário no sistema operacional
# ══════════════════════════════════════════════════════════════════════════════
# Windows: %APPDATA%\hen_sino_cavaco
# Linux/Mac: ~/hen_sino_cavaco
PASTA_APPDATA = os.path.join(
    os.environ.get("APPDATA", os.path.expanduser("~")),
    "hen_sino_cavaco"
)

# ══════════════════════════════════════════════════════════════════════════════
# APLICAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
ID_APP      = "hen-sino-cavaco"
VERSAO_APP  = "v0.1.0"
TITULO_APP  = "hen-sino-Cavaco"
TEMA_QT     = "Fusion"             # tema base do Qt

# Caminhos absolutos — independentes do CWD de execução
_PROJETO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGEM_ICO   = os.path.join(_PROJETO_DIR, "IMAGENS", "icon.ico")
LOGO_MARCA   = os.path.join(_PROJETO_DIR, "IMAGENS", "logo_nome.png")
LOGO_SIMB    = os.path.join(_PROJETO_DIR, "IMAGENS", "logo.png")

# ══════════════════════════════════════════════════════════════════════════════
# FONTES
# ══════════════════════════════════════════════════════════════════════════════
FONTE_NOME_UI       = "Segoe UI"
FONTE_TAMANHO_BASE  = 10     # pontos — fonte padrão da QApplication

FONTE_TAMANHO_TITULO  = 13   # px (CSS/QSS)
FONTE_TAMANHO_INFO    = 14
FONTE_TAMANHO_LABEL   = 13
FONTE_TAMANHO_DETALHE = 12
FONTE_TAMANHO_SUTIL   = 11

# ══════════════════════════════════════════════════════════════════════════════
# JANELA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
LARGURA_PADRAO = 1280
ALTURA_PADRAO  = 800
LARGURA_MIN    = 1024
ALTURA_MIN     = 600
LARGURA_SIDEBAR = 220
MARGEM_PAGINA = 32
ESPACAMENTO_PAGINA = 24
ESPACAMENTO_CARD = 16
PADDING_CARD = 20
ALTURA_BOTAO_NAV = 44
CONFIG_LARGURA_DIALOGO = 680
CONFIG_ALTURA_DIALOGO = 560
CONFIG_LARGURA_MIN_DIALOGO = 560
CONFIG_ALTURA_MIN_DIALOGO = 480
CONFIG_ESPACAMENTO = 10
CONFIG_TAMANHO_ICONE = 18
CONFIG_TAMANHO_AMOSTRA = 24

# Diagrama de acorde de referência
DIAGRAMA_LARGURA = 340
DIAGRAMA_ALTURA = 390
DIAGRAMA_MARGEM_ESQUERDA = 48
DIAGRAMA_TOPO = 76
DIAGRAMA_PASSO_CORDA = 58
DIAGRAMA_PASSO_CASA = 46
DIAGRAMA_NUMERO_CASAS = 5
DIAGRAMA_RAIO_DEDO = 15
DIAGRAMA_RAIO_CORDA_SOLTA = 8

# ══════════════════════════════════════════════════════════════════════════════
# ATALHOS
# ══════════════════════════════════════════════════════════════════════════════
ATALHO_SAIR           = "Alt+F4"
ATALHO_SALVAR         = "Ctrl+S"
ATALHO_ABRIR          = "Ctrl+O"
ATALHO_NOVO           = "Ctrl+N"
# Adicione atalhos específicos do projeto abaixo

# ══════════════════════════════════════════════════════════════════════════════
# CORES — paleta base (nomes semânticos)
# ══════════════════════════════════════════════════════════════════════════════
PRETO          = "#020202"
PRETO_FOSCO    = "#070706"
CINZA_ESCURO   = "#0F1210"
BRANCO         = "#FFF9F2"
AMARELO        = "#E9B968"
AMBAR          = "#8C5538"
AZUL_CLARO     = "#2196F3"
AZUL           = "#0057FF"
AZUL_ESCURO    = "#1FB8D0"
CORAL          = "#FF6B6B"
VERMELHO       = "#A10510"
LARANJA_ESCURO = "#9E3B02"

# ══════════════════════════════════════════════════════════════════════════════
# CORES — UI principal (usadas nos estilos QSS abaixo)
# ══════════════════════════════════════════════════════════════════════════════
COR_BG_APP           = "#F1E8DC"   # linho quente para leitura prolongada
COR_BG_SECUNDARIO    = "#3B2922"   # madeira escura da navegação
COR_BG_TERCIARIO     = "#F8F1E8"   # superfícies em creme suave
COR_BG_CAMPO         = "#FBF6EF"   # campos em papel aquecido
COR_BG_ESCURO        = "#2B201B"   # texto/contraste escuro
COR_BORDA            = "#DED0C1"   # divisórias suaves
COR_BORDA_CLARA      = "#CBB6A3"   # contornos de controles
COR_TEXTO            = "#35271F"   # texto principal
COR_TEXTO_SECUNDARIO = "#66564C"   # texto secundário legível
COR_TEXTO_SUTIL      = "#7D6B60"   # texto auxiliar
COR_TEXTO_INATIVO    = "#948377"   # itens inativos
COR_TEXTO_SIDEBAR    = "#FAF2E8"
COR_TEXTO_SIDEBAR_SUAVE = "#DCCBC0"
COR_ACENTO           = "#A65339"   # terracota
COR_ACENTO_HOVER     = "#B86447"
COR_ACENTO_ATIVO     = "#694033"   # hover/seleção na navegação
COR_ACENTO_BORDA     = "#D6A187"
COR_SUCESSO          = "#89643D"   # ocre, sem verde
COR_SUCESSO_HOVER    = "#73512F"
COR_PERIGO           = "#a10510"
COR_BG_HERO          = "#F8F0E6"
COR_BG_BADGE         = "#EFE0D1"
COR_BORDA_BADGE      = "#E1CCBA"
COR_BG_NAV_BOTAO     = "#49352D"
COR_BORDA_NAV_BOTAO  = "#5A4438"
COR_BORDA_SIDEBAR    = "#514037"
COR_FOCO             = "#D6A187"

# ══════════════════════════════════════════════════════════════════════════════
# TEMAS PERSONALIZÁVEIS
# ══════════════════════════════════════════════════════════════════════════════
def _rgb(cor):
    valor = cor.lstrip("#")
    return tuple(int(valor[i:i + 2], 16) for i in (0, 2, 4))


def _hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(
        *(max(0, min(255, round(c))) for c in rgb)
    )


def _misturar(cor_a, cor_b, proporcao):
    a = _rgb(cor_a)
    b = _rgb(cor_b)
    return _hex(tuple(x + (y - x) * proporcao for x, y in zip(a, b)))


def _luminancia(cor):
    canais = []
    for canal in _rgb(cor):
        valor = canal / 255
        canais.append(
            valor / 12.92 if valor <= 0.04045
            else ((valor + 0.055) / 1.055) ** 2.4
        )
    return 0.2126 * canais[0] + 0.7152 * canais[1] + 0.0722 * canais[2]


def _texto_contraste(cor):
    return "#F7F0E7" if _luminancia(cor) < 0.42 else "#2B211B"


def _criar_paleta(fundo, superficie, menu, texto, destaque):
    texto_menu = _texto_contraste(menu)
    return {
        "fundo": fundo,
        "superficie": superficie,
        "campo": _misturar(superficie, _texto_contraste(superficie), 0.06),
        "menu": menu,
        "texto": texto,
        "texto_secundario": _misturar(texto, fundo, 0.22),
        "texto_sutil": _misturar(texto, fundo, 0.38),
        "texto_inativo": _misturar(texto, fundo, 0.52),
        "texto_menu": texto_menu,
        "texto_menu_suave": _misturar(texto_menu, menu, 0.28),
        "destaque": destaque,
        "destaque_hover": _misturar(destaque, _texto_contraste(destaque), 0.13),
        "destaque_ativo": _misturar(menu, destaque, 0.58),
        "destaque_borda": _misturar(destaque, _texto_contraste(destaque), 0.32),
        "sucesso": "#B18A54" if _luminancia(fundo) < 0.42 else "#89643D",
        "sucesso_hover": "#D0A76C" if _luminancia(fundo) < 0.42 else "#73512F",
        "perigo": "#E17C76" if _luminancia(fundo) < 0.42 else "#A10510",
        "hero": superficie,
        "badge": _misturar(superficie, destaque, 0.16),
        "badge_borda": _misturar(superficie, destaque, 0.30),
        "nav_botao": _misturar(menu, texto_menu, 0.08),
        "nav_borda": _misturar(menu, texto_menu, 0.18),
        "borda": _misturar(fundo, texto, 0.16),
        "borda_controle": _misturar(superficie, texto, 0.28),
        "borda_menu": _misturar(menu, texto_menu, 0.14),
        "foco": _misturar(destaque, _texto_contraste(destaque), 0.48),
        "texto_destaque": _texto_contraste(destaque),
        "destaque_pressionado": _misturar(destaque, fundo, 0.20),
    }


TEMAS_PREDEFINIDOS = {
    "noite_madeira": {
        "nome": "Noite de madeira",
        "cores": _criar_paleta(
            "#292421", "#37302A", "#201A17", "#F4EADF", "#C67855"
        ),
    },
    "papel_suave": {
        "nome": "Papel suave",
        "cores": _criar_paleta(
            "#D8CBBB", "#E8DED0", "#392820", "#30261F", "#9A4B34"
        ),
    },
    "contraste": {
        "nome": "Contraste elevado",
        "cores": _criar_paleta(
            "#F1E6D6", "#FFF3E2", "#191715", "#1B1715", "#7A2F16"
        ),
    },
}

TEMA_PADRAO = {
    "versao": 1,
    "preset": "noite_madeira",
    "cores": TEMAS_PREDEFINIDOS["noite_madeira"]["cores"],
}


def normalizar_tema(dados):
    """Valida o JSON do tema e completa cores ausentes com o tema padrão."""
    if not isinstance(dados, dict):
        dados = {}

    preset = dados.get("preset", TEMA_PADRAO["preset"])
    if preset not in TEMAS_PREDEFINIDOS and preset != "personalizado":
        preset = "personalizado"

    base = TEMAS_PREDEFINIDOS.get(preset, TEMAS_PREDEFINIDOS[
        TEMA_PADRAO["preset"]
    ])["cores"]
    fornecidas = dados.get("cores", {})
    if not isinstance(fornecidas, dict):
        fornecidas = {}

    cores = {}
    for nome, padrao in base.items():
        valor = fornecidas.get(nome, padrao)
        if isinstance(valor, str) and re.fullmatch(r"#[0-9A-Fa-f]{6}", valor):
            cores[nome] = valor.upper()
        else:
            cores[nome] = padrao

    return {"versao": 1, "preset": preset, "cores": cores}


def criar_tema_personalizado(cores_base):
    """Deriva cores auxiliares a partir das cinco cores escolhidas pelo usuário."""
    padrao = TEMAS_PREDEFINIDOS[TEMA_PADRAO["preset"]]["cores"]
    selecionadas = {
        chave: cores_base.get(chave, padrao[chave])
        for chave in ("fundo", "superficie", "menu", "texto", "destaque")
    }
    return normalizar_tema({
        "versao": 1,
        "preset": "personalizado",
        "cores": _criar_paleta(
            selecionadas["fundo"],
            selecionadas["superficie"],
            selecionadas["menu"],
            selecionadas["texto"],
            selecionadas["destaque"],
        ),
    })


# ══════════════════════════════════════════════════════════════════════════════
# CONTEÚDO E IDENTIDADE DO PRIMEIRO PROTÓTIPO
# ══════════════════════════════════════════════════════════════════════════════
TEXTOS_UI = {
    "marca": "hen-sino-Cavaco",
    "submarca": "ESTUDO PASSO A PASSO",
    "header_titulo": "SEU ESPAÇO DE ESTUDO",
    "nav_inicio": "Início",
    "nav_trilha": "Trilha de aprendizagem",
    "nav_acordes": "Acordes",
    "nav_config": "Configurações",
    "rodape_afinação": "Referência: Ré–Sol–Si–Ré",
    "home_selo": "MÉTODO DE ESTUDO DE CAVAQUINHO",
    "home_titulo": "Cavaquinho, um passo de cada vez.",
    "home_descricao": (
        "Um caminho simples para estudar acordes, treinar as trocas e tocar "
        "samba e pagode no seu ritmo."
    ),
    "home_botao_trilha": "Ver trilha de estudo",
    "home_secao_trilha": "Seu caminho para tocar",
    "home_secao_catalogo": "Acordes com clareza",
    "home_catalogo": (
        "Explore os 28 acordes candidatos. Cada seleção abre o diagrama e mostra "
        "cordas, casas, dedos e notas para a afinação de referência."
    ),
    "home_status_catalogo": "VER MATRIZ DE ACORDES",
    "home_numero_fundamentos": "01",
    "home_card_fundamentos": "Fundamentos",
    "home_card_fundamentos_desc": "Afinação, cordas e leitura dos diagramas.",
    "home_numero_acordes": "02",
    "home_card_acordes": "Acordes iniciais",
    "home_card_acordes_desc": "Poucas formas por etapa, testadas no instrumento.",
    "home_numero_ritmo": "03",
    "home_card_ritmo": "Ritmo e música",
    "home_card_ritmo_desc": "Trocas no pulso e aplicação em samba e pagode.",
    "trilha_selo": "ETAPAS DE ESTUDO",
    "trilha_titulo": "Sua trilha de aprendizagem",
    "trilha_descricao": (
        "Uma sequência de referência para estudar por partes. Esta versão ainda "
        "não registra o progresso."
    ),
    "status_agora": "PONTO DE PARTIDA",
    "status_depois": "PRÓXIMA ETAPA",
    "status_futuro": "MAIS ADIANTE",
    "etapa_1": "Conhecer o instrumento e ler um diagrama",
    "etapa_1_desc": "Afinação, cordas, casas e numeração dos dedos.",
    "etapa_2": "Montar os primeiros acordes",
    "etapa_2_desc": "Posições confortáveis e som limpo, uma por vez.",
    "etapa_3": "Trocar acordes sem perder o pulso",
    "etapa_3_desc": "Prática lenta, repetição e pequenas progressões.",
    "etapa_4": "Acompanhar samba e pagode",
    "etapa_4_desc": "Levada simples aplicada a uma música.",
    "etapa_5": "Ampliar para o nível intermediário",
    "etapa_5_desc": "Novas variações quando as bases estiverem firmes.",
    "etapa_6": "Chegar aos recursos avançados",
    "etapa_6_desc": "Inversões, pestanas e transposição em contexto.",
    "acordes_selo": "CATÁLOGO VISUAL · 28 POSIÇÕES CANDIDATAS",
    "acordes_titulo": "Escolha um acorde para ver o diagrama",
    "acordes_descricao": (
        "A matriz organiza sete fundamentais em quatro categorias. Clique em "
        "uma cifra para ver as casas, os dedos e as notas de cada corda."
    ),
    "acordes_aviso_titulo": "As formas ainda são candidatas",
    "acordes_aviso_texto": (
        "As notas foram conferidas por cálculo usando Ré–Sol–Si–Ré. As formas "
        "ainda precisam de confirmação em fontes independentes e teste no "
        "instrumento; nenhuma está marcada como fácil ou definitiva."
    ),
    "acordes_matriz_titulo": "Matriz candidata · 7 × 4",
    "acordes_matriz_instrucao": (
        "Selecione qualquer célula. A linha “sustenida” e a linha “com sétima” "
        "seguem interpretações provisórias."
    ),
    "acordes_coluna_fundamental": "Fundamental",
    "acordes_status_candidata": "CANDIDATA",
    "acordes_diagrama_legenda": (
        "4ª corda à esquerda e 1ª à direita. Os números nos pontos indicam "
        "os dedos da mão esquerda."
    ),
    "acordes_afinação": "Afinação",
    "acordes_casas": "Casas (4ª→1ª)",
    "acordes_dedos": "Dedos (4ª→1ª)",
    "acordes_notas_titulo": "Notas que soam",
    "acordes_cordas_titulo": "Detalhe por corda",
    "acorde_bm_nome": "Si menor",
    "acorde_bm_cifra": "Bm",
    "acorde_bm_status": "Exemplo conferido",
    "acorde_bm_observacao": (
        "A posição abaixo foi lida da imagem enviada. Ela serve para "
        "demonstrar a legenda, não como recomendação de primeiro acorde."
    ),
    "afinação_titulo": "Afinação de referência",
    "afinação_detalhe": "1ª Ré  ·  2ª Si  ·  3ª Sol  ·  4ª Ré",
    "notas_acorde_titulo": "Onde ficam os dedos",
    "texto_corda_1": "1ª corda · Ré · dedo 3 · 4ª casa",
    "texto_corda_2": "2ª corda · Si · dedo 1 · 3ª casa",
    "texto_corda_3": "3ª corda · Sol · dedo 2 · 4ª casa",
    "texto_corda_4": "4ª corda · Ré solta",
    "diagrama_legenda": "No desenho: 4ª corda à esquerda, 1ª à direita.",
    "status_pronto": "Protótipo · conteúdo em validação",
}

TEXTOS_CONFIGURACOES = {
    "titulo": "Cores do aplicativo",
    "descricao": (
        "Escolha uma paleta pronta ou ajuste as cores. Sua escolha fica salva "
        "neste computador e será usada na próxima abertura."
    ),
    "seletor_tema": "Paleta",
    "cores_principais": "Personalize as cores principais",
    "fundo": "Fundo da página",
    "superficie": "Painéis e cartões",
    "menu": "Menu lateral",
    "texto": "Texto principal",
    "destaque": "Destaque e botões",
    "escolher_cor": "Escolher cor",
    "previa": "Prévia do tema",
    "previa_titulo": "Leitura de exemplo",
    "previa_texto": "Este texto mostra como a leitura ficará no aplicativo.",
    "restaurar": "Tema inicial",
    "cancelar": "Cancelar",
    "aplicar": "Aplicar e salvar",
    "personalizado": "Personalizado",
    "tooltip": "Personalizar cores do aplicativo",
    "aviso_contraste": (
        "A combinação de fundo e texto pode dificultar a leitura. "
        "Escolha cores mais contrastantes."
    ),
    "salvo": "Cores atualizadas e salvas neste computador.",
    "falha_salvar": "Não foi possível salvar as cores neste computador.",
}

CORES_TEMA_EDITAVEIS = (
    ("fundo", TEXTOS_CONFIGURACOES["fundo"]),
    ("superficie", TEXTOS_CONFIGURACOES["superficie"]),
    ("menu", TEXTOS_CONFIGURACOES["menu"]),
    ("texto", TEXTOS_CONFIGURACOES["texto"]),
    ("destaque", TEXTOS_CONFIGURACOES["destaque"]),
)

ETAPAS_INICIO = (
    (
        TEXTOS_UI["home_numero_fundamentos"],
        TEXTOS_UI["home_card_fundamentos"],
        TEXTOS_UI["home_card_fundamentos_desc"],
    ),
    (
        TEXTOS_UI["home_numero_acordes"],
        TEXTOS_UI["home_card_acordes"],
        TEXTOS_UI["home_card_acordes_desc"],
    ),
    (
        TEXTOS_UI["home_numero_ritmo"],
        TEXTOS_UI["home_card_ritmo"],
        TEXTOS_UI["home_card_ritmo_desc"],
    ),
)

ETAPAS_TRILHA = (
    ("01", TEXTOS_UI["etapa_1"], TEXTOS_UI["etapa_1_desc"], "agora"),
    ("02", TEXTOS_UI["etapa_2"], TEXTOS_UI["etapa_2_desc"], "depois"),
    ("03", TEXTOS_UI["etapa_3"], TEXTOS_UI["etapa_3_desc"], "depois"),
    ("04", TEXTOS_UI["etapa_4"], TEXTOS_UI["etapa_4_desc"], "futuro"),
    ("05", TEXTOS_UI["etapa_5"], TEXTOS_UI["etapa_5_desc"], "futuro"),
    ("06", TEXTOS_UI["etapa_6"], TEXTOS_UI["etapa_6_desc"], "futuro"),
)

# ══════════════════════════════════════════════════════════════════════════════
# EXPLORER — dimensões, textos e filtros do utilitário compartilhado
# ══════════════════════════════════════════════════════════════════════════════
EXPLORER_LARGURA_PADRAO = 1280
EXPLORER_ALTURA_PADRAO = 720
EXPLORER_LARGURA_MIN = 980
EXPLORER_ALTURA_MIN = 500
EXPLORER_LARGURA_LOCAIS = 190
EXPLORER_PREVIEW_TAMANHO = 240
EXPLORER_PREVIEW_ALTURA = 170
EXPLORER_PREVIEW_MAX_BYTES = 30 * 1024 * 1024
EXPLORER_PREVIEW_MAX_PIXELS = 40_000_000
EXPLORER_PREVIEW_MAX_ITEMS = 50_000
EXPLORER_PREVIEW_MAX_SECONDS = 8.0
EXPLORER_PREVIEW_DEBOUNCE_MS = 180
EXPLORER_ESPACAMENTO = 8
EXPLORER_MARGEM = 12
EXPLORER_RAIO_BORDA = 5
EXPLORER_TAMANHO_ICONE = 16
EXPLORER_ALTURA_CONTROLE = 34
EXPLORER_PADDING_H = 9
EXPLORER_PADDING_V = 5
EXPLORER_PADDING_ITEM_H = 7
EXPLORER_PADDING_ITEM_V = 4
EXPLORER_LARGURA_COLUNA_TAMANHO = 100
EXPLORER_LARGURA_COLUNA_TIPO = 150
EXPLORER_LARGURA_COLUNA_DATA = 175

EXPLORER_CABECALHOS = ("Nome", "Tamanho", "Tipo", "Modificado em")

EXPLORER_TEXTOS = {
    "title_open_file": "Abrir arquivo",
    "title_open_files": "Selecionar arquivos",
    "title_select_folder": "Selecionar pasta",
    "title_save_file": "Salvar arquivo",
    "title_manage": "Explorador de arquivos",
    "location": "Local:",
    "path_placeholder": "Digite um caminho e pressione Enter",
    "search_placeholder": "Pesquisar nesta pasta",
    "organize": "Organizar",
    "sort_name": "Nome",
    "sort_size": "Tamanho",
    "sort_type": "Tipo",
    "sort_modified": "Data de modificação",
    "sort_descending": "Ordem decrescente",
    "places": "Locais",
    "place_home": "Início",
    "place_desktop": "Área de Trabalho",
    "place_documents": "Documentos",
    "place_downloads": "Downloads",
    "place_pictures": "Imagens",
    "place_music": "Músicas",
    "place_videos": "Vídeos",
    "place_computer": "Este computador",
    "filename": "Nome:",
    "file_type": "Tipo de arquivo:",
    "show_hidden": "Mostrar itens ocultos",
    "open": "Abrir",
    "select_folder": "Selecionar pasta",
    "save": "Salvar",
    "cancel": "Cancelar",
    "close": "Fechar",
    "new_folder": "Nova pasta",
    "new_folder_title": "Criar pasta",
    "new_folder_prompt": "Nome da nova pasta:",
    "rename": "Renomear",
    "rename_title": "Renomear item",
    "rename_prompt": "Novo nome:",
    "copy_path": "Copiar caminho",
    "move_to_trash": "Mover para a Lixeira",
    "trash_confirm_title": "Mover para a Lixeira?",
    "trash_confirm_message": "O item selecionado será movido para a Lixeira do sistema.",
    "error_title": "Não foi possível concluir",
    "invalid_location": "Esse local não existe ou não pode ser acessado.",
    "invalid_name": "Informe um nome válido, sem separadores de pasta.",
    "empty_filename": "Informe o nome do arquivo.",
    "file_required": "Selecione um arquivo.",
    "save_folder_error": "O nome informado aponta para uma pasta, não para um arquivo.",
    "overwrite_title": "Substituir arquivo?",
    "overwrite_message": "Esse arquivo já existe. Deseja substituí-lo?",
    "new_folder_error": "Não foi possível criar a pasta.",
    "rename_error": "Não foi possível renomear o item.",
    "trash_error": "O sistema não conseguiu mover o item para a Lixeira.",
    "items_count": "{count} itens",
    "items_selected": "{count} selecionados",
    "ready": "Pronto",
    "tooltip_back": "Voltar",
    "tooltip_forward": "Avançar",
    "tooltip_up": "Subir uma pasta",
    "tooltip_home": "Ir para Início",
    "tooltip_refresh": "Atualizar",
    "tooltip_new_folder": "Criar uma pasta neste local",
    "preview_title": "Prévia e propriedades",
    "preview_empty": "Passe o mouse ou selecione um item para ver detalhes.",
    "preview_image_placeholder": "Prévia do item",
    "preview_loading": "Carregando prévia e propriedades...",
    "preview_kind_folder": "Pasta",
    "preview_kind_image": "Imagem",
    "preview_kind_video": "Vídeo",
    "preview_kind_file": "Arquivo",
    "preview_kind_unknown": "Item",
    "preview_folder_details": (
        "{name}\nPasta\nTamanho total: {size}\nArquivos: {files}\n"
        "Subpastas: {folders}\nModificado em: {modified}\n{path}"
    ),
    "preview_file_details": (
        "{name}\n{kind} • {file_type}\nTamanho: {size}\n"
        "Modificado em: {modified}\n{path}"
    ),
    "preview_selected_count": "{count} itens selecionados",
    "preview_partial": "Leitura parcial; alguns itens não foram incluídos.",
    "preview_unavailable": "Não há prévia disponível para este tipo de item.",
    "preview_image_too_large": "Imagem muito grande para gerar uma prévia segura.",
    "preview_image_unreadable": "Não foi possível ler esta imagem.",
    "preview_video_unavailable": "Não foi possível obter uma imagem deste vídeo.",
    "preview_link": "Prévia desativada para links simbólicos.",
}

EXPLORER_FILTROS = (
    ("Todos os arquivos (*)", ("*",)),
    (
        "Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.webp *.tif *.tiff)",
        ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.webp", "*.tif", "*.tiff"),
    ),
    (
        "Vídeos (*.mp4 *.mov *.mkv *.webm *.avi *.m4v)",
        ("*.mp4", "*.mov", "*.mkv", "*.webm", "*.avi", "*.m4v"),
    ),
    (
        "Áudio (*.mp3 *.wav *.flac *.aac *.ogg *.m4a)",
        ("*.mp3", "*.wav", "*.flac", "*.aac", "*.ogg", "*.m4a"),
    ),
)

# ══════════════════════════════════════════════════════════════════════════════
# ESTILOS QSS — prontos para uso direto
# ══════════════════════════════════════════════════════════════════════════════

ESTILO_ESCURO_GLOBAL = f"""
QMainWindow, QWidget#appCanvas {{
    background: {COR_BG_APP};
    color: {COR_TEXTO};
    font-family: "{FONTE_NOME_UI}", Arial, sans-serif;
    font-size: {FONTE_TAMANHO_LABEL}px;
}}
QWidget {{
    color: {COR_TEXTO};
    font-family: "{FONTE_NOME_UI}", Arial, sans-serif;
    font-size: {FONTE_TAMANHO_LABEL}px;
}}
QLabel {{ background: transparent; }}
QStackedWidget, QScrollArea, QScrollArea::viewport {{
    background: {COR_BG_APP};
    border: none;
}}
QWidget#learningPage,
QScrollArea#learningScrollArea,
QWidget#learningViewport,
QWidget#learningContent {{
    background: {COR_BG_APP};
    border: none;
}}
QSplitter::handle {{ background: {COR_BORDA}; }}
QMenuBar {{
    background: {COR_BG_APP};
    color: {COR_TEXTO};
    border-bottom: 1px solid {COR_BORDA};
}}
QMenuBar::item:selected {{
    background: {COR_ACENTO_ATIVO};
    color: {BRANCO};
}}
QMenu {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    border: 1px solid {COR_BORDA_CLARA};
}}
QMenu::item:selected {{
    background: {COR_ACENTO};
    color: {BRANCO};
}}
QToolBar {{
    background: {COR_BG_APP};
    border-bottom: 1px solid {COR_BORDA};
    spacing: 4px;
    padding: 6px;
}}
QToolButton {{
    background: transparent;
    color: {COR_TEXTO};
    border: none;
    padding: 8px 10px;
    border-radius: 8px;
}}
QToolButton:hover   {{ background: {COR_BG_TERCIARIO}; }}
QToolButton:pressed {{ background: {COR_BG_TERCIARIO}; }}
QStatusBar {{
    background: {COR_BG_APP};
    color: {COR_TEXTO_SECUNDARIO};
    border-top: 1px solid {COR_BORDA};
    font-size: {FONTE_TAMANHO_DETALHE}px;
}}
QScrollBar:vertical {{
    background: transparent; width: 10px; border: none;
}}
QScrollBar::handle:vertical {{
    background: {COR_BORDA_CLARA}; border-radius: 5px; min-height: 28px;
}}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{ height: 0; }}
QScrollBar:horizontal {{
    background: transparent; height: 10px; border: none;
}}
QScrollBar::handle:horizontal {{
    background: {COR_BORDA_CLARA}; border-radius: 5px; min-width: 20px;
}}
QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {{ width: 0; }}
"""

ESTILO_APP = f"""
QFrame#appSidebar {{
    background: {COR_BG_SECUNDARIO};
    border-right: 1px solid {COR_BORDA_SIDEBAR};
}}
QFrame#contentHeader {{
    background: transparent;
    border: none;
}}
QLabel#brandTitle {{
    color: {COR_TEXTO_SIDEBAR};
    font-size: 18px;
    font-weight: 700;
}}
QLabel#brandSubtitle {{
    color: {COR_TEXTO_SIDEBAR_SUAVE};
    font-size: {FONTE_TAMANHO_SUTIL}px;
    font-weight: 700;
}}
QLabel#eyebrow {{
    color: {COR_ACENTO};
    font-size: {FONTE_TAMANHO_SUTIL}px;
    font-weight: 700;
}}
QLabel#pageTitle {{
    color: {COR_TEXTO};
    font-size: 28px;
    font-weight: 700;
}}
QLabel#heroTitle {{
    color: {COR_TEXTO};
    font-size: 36px;
    font-weight: 700;
}}
QLabel#sectionTitle {{
    color: {COR_TEXTO};
    font-size: 19px;
    font-weight: 700;
}}
QLabel#bodyText {{
    color: {COR_TEXTO_SECUNDARIO};
    font-size: 14px;
}}
QLabel#mutedText {{
    color: {COR_TEXTO_SUTIL};
    font-size: {FONTE_TAMANHO_DETALHE}px;
}}
QLabel#sidebarFooter {{
    color: {COR_TEXTO_SIDEBAR_SUAVE};
    font-size: {FONTE_TAMANHO_DETALHE}px;
}}
QLabel#chordTitle {{
    color: {COR_TEXTO};
    font-size: 32px;
    font-weight: 700;
}}
QLabel#chordBadge {{
    color: {COR_ACENTO};
    background: {COR_BG_BADGE};
    border: 1px solid {COR_BORDA_BADGE};
    border-radius: 12px;
    padding: 6px 10px;
    font-weight: 700;
}}
QFrame#heroCard {{
    background: {COR_BG_HERO};
    border: 1px solid {COR_BORDA};
    border-left: 5px solid {COR_ACENTO};
    border-radius: 14px;
}}
QFrame#surfaceCard {{
    background: {COR_BG_TERCIARIO};
    border: 1px solid {COR_BORDA};
    border-radius: 14px;
}}
QFrame#pathStep {{
    background: transparent;
    border: none;
}}
QFrame#stepSeparator {{
    background: {COR_BORDA};
    border: none;
    min-width: 1px;
    max-width: 1px;
}}
QFrame#homeCatalog {{
    background: transparent;
    border: none;
    border-top: 1px solid {COR_BORDA};
}}
QFrame#stageCard {{
    background: transparent;
    border: none;
    border-bottom: 1px solid {COR_BORDA};
    border-left: 4px solid transparent;
    border-radius: 0;
}}
QFrame#stageCard[state="current"] {{
    background: transparent;
    border-left: 4px solid {COR_ACENTO};
}}
QFrame#stageCard QLabel {{
    background: transparent;
}}
QLabel#stageNumber {{
    color: {COR_ACENTO};
    background: transparent;
    border: none;
    font-size: 16px;
    font-weight: 700;
}}
QLabel#stepNumber {{
    color: {COR_ACENTO};
    font-size: {FONTE_TAMANHO_DETALHE}px;
    font-weight: 700;
}}
QLabel#homeStatus {{
    color: {COR_ACENTO};
    background: {COR_BG_BADGE};
    border: none;
    border-radius: 10px;
    padding: 7px 10px;
    font-size: {FONTE_TAMANHO_SUTIL}px;
    font-weight: 700;
}}
QPushButton#navButton {{
    color: {COR_TEXTO_SIDEBAR_SUAVE};
    background: {COR_BG_NAV_BOTAO};
    border: 1px solid {COR_BORDA_NAV_BOTAO};
    border-radius: 10px;
    text-align: left;
    padding: 12px 14px;
    font-size: {FONTE_TAMANHO_INFO}px;
}}
QPushButton#navButton:hover {{
    background: {COR_ACENTO_ATIVO};
    color: {COR_TEXTO_SIDEBAR};
}}
QPushButton#navButton:checked {{
    color: {BRANCO};
    background: {COR_ACENTO};
    border: 1px solid {COR_ACENTO};
    font-weight: 700;
}}
QPushButton#navButton:focus {{
    border: 1px solid {COR_FOCO};
}}
QPushButton#settingsButton {{
    color: {COR_TEXTO_SIDEBAR_SUAVE};
    background: {COR_BG_NAV_BOTAO};
    border: 1px solid {COR_BORDA_NAV_BOTAO};
    border-radius: 10px;
    text-align: left;
    padding: 12px 14px;
    font-size: {FONTE_TAMANHO_INFO}px;
}}
QPushButton#settingsButton:hover {{
    color: {COR_TEXTO_SIDEBAR};
    background: {COR_ACENTO_ATIVO};
    border-color: {COR_ACENTO_BORDA};
}}
QPushButton#settingsButton:focus {{
    border: 1px solid {COR_FOCO};
}}
QPushButton#primaryButton {{
    color: {BRANCO};
    background: {COR_ACENTO};
    border: none;
    border-radius: 10px;
    padding: 12px 20px;
    min-height: {ALTURA_BOTAO_NAV}px;
    font-weight: 700;
}}
QPushButton#primaryButton:hover {{
    background: {COR_ACENTO_HOVER};
}}
QPushButton#primaryButton:pressed {{
    background: {AMBAR};
}}
QPushButton#primaryButton:focus {{
    border: 2px solid {COR_FOCO};
}}
"""

ESTILO_CONFIGURACOES = f"""
QDialog#settingsDialog {{
    background: {COR_BG_APP};
    color: {COR_TEXTO};
}}
QFrame#themePreview {{
    background: {COR_BG_TERCIARIO};
    border: 1px solid {COR_BORDA};
    border-radius: 12px;
}}
QScrollArea#settingsScrollArea,
QWidget#settingsContent {{
    background: transparent;
    border: none;
}}
QComboBox#themePresetCombo {{
    background: {COR_BG_CAMPO};
    color: {COR_TEXTO};
    border: 1px solid {COR_BORDA_CLARA};
    border-radius: 8px;
    padding: 8px 10px;
    min-height: 28px;
}}
QComboBox#themePresetCombo QAbstractItemView {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    selection-background-color: {COR_ACENTO};
    selection-color: {BRANCO};
}}
QPushButton#settingsColorButton,
QPushButton#settingsRestoreButton,
QPushButton#settingsCancelButton {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    border: 1px solid {COR_BORDA_CLARA};
    border-radius: 8px;
    padding: 8px 12px;
    min-height: 28px;
}}
QPushButton#settingsColorButton:hover,
QPushButton#settingsRestoreButton:hover,
QPushButton#settingsCancelButton:hover {{
    background: {COR_BG_CAMPO};
    border-color: {COR_ACENTO_BORDA};
}}
QPushButton#settingsApplyButton,
QPushButton#themePreviewPrimaryButton {{
    background: {COR_ACENTO};
    color: {BRANCO};
    border: none;
    border-radius: 8px;
    padding: 9px 16px;
    min-height: 30px;
    font-weight: 700;
}}
QPushButton#settingsApplyButton:hover,
QPushButton#themePreviewPrimaryButton:hover {{
    background: {COR_ACENTO_HOVER};
}}
QLabel#settingsWarning {{
    color: {COR_PERIGO};
    font-weight: 700;
}}
"""


def estilos_para_tema(tema):
    """Gera a folha de estilos principal usando o tema do usuário."""
    cores = normalizar_tema(tema)["cores"]
    substituicoes = {
        COR_BG_APP: cores["fundo"],
        COR_BG_SECUNDARIO: cores["menu"],
        COR_BG_TERCIARIO: cores["superficie"],
        COR_BG_CAMPO: cores["campo"],
        COR_BG_ESCURO: cores["texto"],
        COR_BORDA: cores["borda"],
        COR_BORDA_CLARA: cores["borda_controle"],
        COR_TEXTO: cores["texto"],
        COR_TEXTO_SECUNDARIO: cores["texto_secundario"],
        COR_TEXTO_SUTIL: cores["texto_sutil"],
        COR_TEXTO_INATIVO: cores["texto_inativo"],
        COR_TEXTO_SIDEBAR: cores["texto_menu"],
        COR_TEXTO_SIDEBAR_SUAVE: cores["texto_menu_suave"],
        COR_ACENTO: cores["destaque"],
        COR_ACENTO_HOVER: cores["destaque_hover"],
        COR_ACENTO_ATIVO: cores["destaque_ativo"],
        COR_ACENTO_BORDA: cores["destaque_borda"],
        COR_SUCESSO: cores["sucesso"],
        COR_SUCESSO_HOVER: cores["sucesso_hover"],
        COR_PERIGO: cores["perigo"],
        COR_BG_HERO: cores["hero"],
        COR_BG_BADGE: cores["badge"],
        COR_BORDA_BADGE: cores["badge_borda"],
        COR_BG_NAV_BOTAO: cores["nav_botao"],
        COR_BORDA_NAV_BOTAO: cores["nav_borda"],
        COR_BORDA_SIDEBAR: cores["borda_menu"],
        COR_FOCO: cores["foco"],
        BRANCO: cores["texto_destaque"],
        AMBAR: cores["destaque_pressionado"],
    }
    substituicoes = {
        origem.upper(): destino.upper()
        for origem, destino in substituicoes.items()
    }
    base = "\n".join((
        ESTILO_ESCURO_GLOBAL,
        ESTILO_APP,
        ESTILO_CONFIGURACOES,
    ))
    return re.sub(
        r"#[0-9A-Fa-f]{6}",
        lambda achado: substituicoes.get(
            achado.group(0).upper(), achado.group(0)
        ),
        base,
    )


ESTILO_DIALOGO_ESCURO = f"""
QDialog    {{ background: {COR_BG_CAMPO}; color: {COR_TEXTO}; }}
QLabel     {{ color: {COR_TEXTO_SECUNDARIO}; }}
QGroupBox  {{
    color: {COR_TEXTO_SECUNDARIO};
    border: 1px solid {COR_BORDA};
    border-radius: 4px;
    margin-top: 8px;
    font-size: {FONTE_TAMANHO_LABEL}px;
}}
QGroupBox::title {{ subcontrol-origin: margin; left: 8px; padding: 0 4px; }}
QComboBox, QSpinBox, QLineEdit, QDoubleSpinBox {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    border: 1px solid {COR_BORDA_CLARA};
    border-radius: 3px;
    padding: 3px;
}}
"""

ESTILO_BTN_PRIMARIO = f"""
QPushButton {{
    background: {COR_ACENTO};
    color: {BRANCO};
    border: none;
    padding: 8px 20px;
    border-radius: 4px;
    font-size: {FONTE_TAMANHO_INFO}px;
    font-weight: bold;
}}
QPushButton:hover    {{ background: {COR_ACENTO_HOVER}; }}
QPushButton:disabled {{ background: {COR_BG_TERCIARIO}; color: {COR_TEXTO_INATIVO}; }}
"""

ESTILO_BTN_CANCELAR = f"""
QPushButton {{
    background: {COR_BORDA_CLARA};
    color: {COR_TEXTO_SECUNDARIO};
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
}}
QPushButton:hover {{ background: {COR_TEXTO_SUTIL}; }}
"""

ESTILO_LIST_WIDGET = f"""
QListWidget {{
    background: {COR_BG_APP};
    border: none;
    color: {COR_TEXTO};
}}
QListWidget::item {{ padding: 4px; border-bottom: 1px solid {COR_BORDA}; }}
QListWidget::item:selected {{
    background: {COR_ACENTO};
    color: {BRANCO};
}}
QListWidget::item:hover    {{ background: {COR_BG_TERCIARIO}; }}
"""

ESTILO_PROGRESSBAR = f"""
QProgressBar {{
    background: {COR_BG_TERCIARIO};
    border: 1px solid {COR_BORDA_CLARA};
    border-radius: 3px;
}}
QProgressBar::chunk {{
    background: {COR_ACENTO};
    border-radius: 2px;
}}
"""

ESTILO_EXPLORER = f"""
QDialog#explorerDialog {{
    background: {COR_BG_CAMPO};
    color: {COR_TEXTO};
}}
QFrame#explorerToolbar, QFrame#explorerFooter {{
    background: {COR_BG_TERCIARIO};
    border: 1px solid {COR_BORDA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
}}
QToolButton#explorerNavigationButton {{
    background: transparent;
    color: {COR_TEXTO};
    border: none;
    border-radius: {EXPLORER_RAIO_BORDA}px;
    padding: {EXPLORER_PADDING_V}px;
}}
QToolButton#explorerNavigationButton:hover {{
    background: {COR_BG_TERCIARIO};
}}
QListWidget#explorerPlaces {{
    background: {COR_BG_CAMPO};
    border: 1px solid {COR_BORDA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
    outline: none;
}}
QListWidget#explorerPlaces::item {{
    padding: {EXPLORER_PADDING_ITEM_V}px {EXPLORER_PADDING_ITEM_H}px;
    border-radius: {EXPLORER_RAIO_BORDA}px;
}}
QListWidget#explorerPlaces::item:selected {{
    background: {COR_ACENTO};
    color: {BRANCO};
}}
QFrame#explorerPlacesSeparator {{
    background: {COR_BORDA};
    border: none;
    max-height: 1px;
    min-height: 1px;
    margin: 4px 8px;
}}
QFrame#explorerPreviewPanel {{
    background: {COR_BG_TERCIARIO};
    border: 1px solid {COR_BORDA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
}}
QLabel#explorerPreviewTitle {{
    color: {COR_TEXTO};
    font-weight: bold;
}}
QLabel#explorerPreviewImage {{
    background: {COR_BG_APP};
    color: {COR_TEXTO_SECUNDARIO};
    border: 1px solid {COR_BORDA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
}}
QLabel#explorerPreviewDetails {{ color: {COR_TEXTO}; }}
QTreeView#explorerFileView {{
    background: {COR_BG_APP};
    alternate-background-color: {COR_BG_CAMPO};
    border: 1px solid {COR_BORDA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
    outline: none;
}}
QTreeView#explorerFileView::item {{
    padding: {EXPLORER_PADDING_ITEM_V}px {EXPLORER_PADDING_ITEM_H}px;
}}
QTreeView#explorerFileView::item:selected {{
    background: {COR_ACENTO};
    color: {BRANCO};
}}
QHeaderView::section {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    border: none;
    border-bottom: 1px solid {COR_BORDA};
    padding: {EXPLORER_PADDING_V}px {EXPLORER_PADDING_H}px;
    font-size: {FONTE_TAMANHO_DETALHE}px;
}}
QComboBox#explorerPathInput, QLineEdit#explorerPathInput,
QLineEdit#explorerSearchInput,
QLineEdit#explorerFilenameInput, QComboBox#explorerFilterCombo {{
    background: {COR_BG_TERCIARIO};
    color: {COR_TEXTO};
    border: 1px solid {COR_BORDA_CLARA};
    border-radius: {EXPLORER_RAIO_BORDA}px;
    padding: {EXPLORER_PADDING_V}px {EXPLORER_PADDING_H}px;
    min-height: {EXPLORER_ALTURA_CONTROLE}px;
}}
QComboBox#explorerPathInput:focus, QLineEdit#explorerPathInput:focus,
QLineEdit#explorerSearchInput:focus,
QLineEdit#explorerFilenameInput:focus, QComboBox#explorerFilterCombo:focus {{
    border: 1px solid {COR_ACENTO_BORDA};
}}
QPushButton#explorerPrimaryButton {{
    background: {COR_ACENTO};
    color: {BRANCO};
    border: none;
    border-radius: {EXPLORER_RAIO_BORDA}px;
    padding: {EXPLORER_PADDING_V}px {EXPLORER_PADDING_H * 2}px;
    min-height: {EXPLORER_ALTURA_CONTROLE}px;
    font-size: {FONTE_TAMANHO_INFO}px;
    font-weight: bold;
}}
QPushButton#explorerPrimaryButton:hover {{
    background: {COR_ACENTO_HOVER};
}}
QPushButton#explorerCancelButton {{
    background: {COR_BORDA_CLARA};
    color: {COR_TEXTO};
    border: none;
    border-radius: {EXPLORER_RAIO_BORDA}px;
    padding: {EXPLORER_PADDING_V}px {EXPLORER_PADDING_H * 2}px;
    min-height: {EXPLORER_ALTURA_CONTROLE}px;
}}
QPushButton#explorerCancelButton:hover {{
    background: {COR_TEXTO_SUTIL};
}}
QLabel#explorerStatusLabel {{
    color: {COR_TEXTO_SECUNDARIO};
    font-size: {FONTE_TAMANHO_DETALHE}px;
}}
"""
