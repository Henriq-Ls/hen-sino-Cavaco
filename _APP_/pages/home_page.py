from _CONFIGURA_ import (
    ETAPAS_INICIO,
    ESPACAMENTO_CARD,
    ESPACAMENTO_PAGINA,
    MARGEM_PAGINA,
    PADDING_CARD,
    TEXTOS_UI,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class HomePage(QWidget):
    abrir_trilha = Signal()
    abrir_acordes = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("homePage")
        self._montar_ui()

    def _montar_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            MARGEM_PAGINA, MARGEM_PAGINA, MARGEM_PAGINA, MARGEM_PAGINA
        )
        layout.setSpacing(ESPACAMENTO_PAGINA)

        hero = QFrame()
        hero.setObjectName("heroCard")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(
            PADDING_CARD * 2, PADDING_CARD * 2,
            PADDING_CARD * 2, PADDING_CARD * 2,
        )
        hero_layout.setSpacing(ESPACAMENTO_CARD)

        eyebrow = QLabel(TEXTOS_UI["home_selo"])
        eyebrow.setObjectName("eyebrow")
        title = QLabel(TEXTOS_UI["home_titulo"])
        title.setObjectName("heroTitle")
        title.setWordWrap(True)
        description = QLabel(TEXTOS_UI["home_descricao"])
        description.setObjectName("bodyText")
        description.setWordWrap(True)

        button = QPushButton(TEXTOS_UI["home_botao_trilha"])
        button.setObjectName("primaryButton")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        button.clicked.connect(self.abrir_trilha)

        hero_layout.addWidget(eyebrow)
        hero_layout.addWidget(title)
        hero_layout.addWidget(description)
        hero_layout.addSpacing(ESPACAMENTO_CARD)
        hero_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(hero)

        section_title = QLabel(TEXTOS_UI["home_secao_trilha"])
        section_title.setObjectName("sectionTitle")
        layout.addWidget(section_title)

        steps = QHBoxLayout()
        steps.setContentsMargins(0, 0, 0, 0)
        steps.setSpacing(0)
        for index, etapa in enumerate(ETAPAS_INICIO):
            if index:
                steps.addSpacing(ESPACAMENTO_CARD)
                separator = QFrame()
                separator.setObjectName("stepSeparator")
                separator.setFixedHeight(PADDING_CARD * 4)
                steps.addWidget(
                    separator,
                    alignment=Qt.AlignmentFlag.AlignVCenter,
                )
                steps.addSpacing(ESPACAMENTO_CARD)
            steps.addWidget(self._step(*etapa), stretch=1)
        layout.addLayout(steps)

        catalog = QFrame()
        catalog.setObjectName("homeCatalog")
        catalog_layout = QHBoxLayout(catalog)
        catalog_layout.setContentsMargins(0, PADDING_CARD, 0, 0)
        catalog_layout.setSpacing(ESPACAMENTO_CARD)

        catalog_text = QVBoxLayout()
        catalog_text.setContentsMargins(0, 0, 0, 0)
        catalog_text.setSpacing(ESPACAMENTO_CARD // 2)
        catalog_title = QLabel(TEXTOS_UI["home_secao_catalogo"])
        catalog_title.setObjectName("sectionTitle")
        catalog_description = QLabel(TEXTOS_UI["home_catalogo"])
        catalog_description.setObjectName("bodyText")
        catalog_description.setWordWrap(True)
        catalog_text.addWidget(catalog_title)
        catalog_text.addWidget(catalog_description)

        catalog_status = QPushButton(TEXTOS_UI["home_status_catalogo"])
        catalog_status.setObjectName("primaryButton")
        catalog_status.setCursor(Qt.CursorShape.PointingHandCursor)
        catalog_status.clicked.connect(self.abrir_acordes)
        catalog_layout.addLayout(catalog_text, stretch=1)
        catalog_layout.addWidget(
            catalog_status,
            alignment=Qt.AlignmentFlag.AlignVCenter,
        )
        layout.addWidget(catalog)
        layout.addStretch(1)

    @staticmethod
    def _step(numero, titulo, descrição):
        step = QFrame()
        step.setObjectName("pathStep")
        step_layout = QVBoxLayout(step)
        step_layout.setContentsMargins(0, 0, 0, 0)
        step_layout.setSpacing(ESPACAMENTO_CARD // 2)

        number = QLabel(f"PASSO {numero}")
        number.setObjectName("stepNumber")
        title = QLabel(titulo)
        title.setObjectName("sectionTitle")
        title.setWordWrap(True)
        text = QLabel(descrição)
        text.setObjectName("bodyText")
        text.setWordWrap(True)

        step_layout.addWidget(number)
        step_layout.addWidget(title)
        step_layout.addWidget(text)
        step_layout.addStretch(1)
        return step
