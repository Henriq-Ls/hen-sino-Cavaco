from _CONFIGURA_ import (
    ETAPAS_TRILHA,
    ESPACAMENTO_CARD,
    ESPACAMENTO_PAGINA,
    MARGEM_PAGINA,
    PADDING_CARD,
    TEXTOS_UI,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class LearningPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("learningPage")
        self._montar_ui()

    def _montar_ui(self):
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setObjectName("learningScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.viewport().setObjectName("learningViewport")
        content = QWidget()
        content.setObjectName("learningContent")
        layout = QVBoxLayout(content)
        layout.setContentsMargins(
            MARGEM_PAGINA, MARGEM_PAGINA, MARGEM_PAGINA, MARGEM_PAGINA
        )
        layout.setSpacing(ESPACAMENTO_PAGINA)

        eyebrow = QLabel(TEXTOS_UI["trilha_selo"])
        eyebrow.setObjectName("eyebrow")
        title = QLabel(TEXTOS_UI["trilha_titulo"])
        title.setObjectName("pageTitle")
        description = QLabel(TEXTOS_UI["trilha_descricao"])
        description.setObjectName("bodyText")
        description.setWordWrap(True)

        layout.addWidget(eyebrow)
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(ESPACAMENTO_CARD)

        for numero, título, descrição, estado in ETAPAS_TRILHA:
            layout.addWidget(self._etapa(numero, título, descrição, estado))

        layout.addStretch(1)
        scroll.setWidget(content)
        page_layout.addWidget(scroll)

    @staticmethod
    def _etapa(numero, título, descrição, estado):
        card = QFrame()
        card.setObjectName("stageCard")
        card.setProperty("state", "current" if estado == "agora" else "later")

        row = QHBoxLayout(card)
        row.setContentsMargins(
            PADDING_CARD, PADDING_CARD, PADDING_CARD, PADDING_CARD
        )
        row.setSpacing(ESPACAMENTO_CARD)

        number = QLabel(numero)
        number.setObjectName("stageNumber")
        number.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        number.setFixedWidth(PADDING_CARD * 3)

        text_column = QVBoxLayout()
        text_column.setSpacing(ESPACAMENTO_CARD // 2)
        title = QLabel(título)
        title.setObjectName("sectionTitle")
        detail = QLabel(descrição)
        detail.setObjectName("bodyText")
        detail.setWordWrap(True)
        text_column.addWidget(title)
        text_column.addWidget(detail)

        status_text = {
            "agora": TEXTOS_UI["status_agora"],
            "depois": TEXTOS_UI["status_depois"],
            "futuro": TEXTOS_UI["status_futuro"],
        }[estado]
        status = QLabel(status_text)
        status.setObjectName("eyebrow" if estado == "agora" else "mutedText")
        status.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        row.addWidget(number, alignment=Qt.AlignmentFlag.AlignTop)
        row.addLayout(text_column, stretch=1)
        row.addWidget(status, alignment=Qt.AlignmentFlag.AlignTop)
        return card
