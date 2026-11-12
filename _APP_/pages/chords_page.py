from _CONFIGURA_ import (
    ESPACAMENTO_CARD,
    ESPACAMENTO_PAGINA,
    MARGEM_PAGINA,
    PADDING_CARD,
    TEMA_PADRAO,
    TEXTOS_UI,
)
from ACORDES.referencias import CATEGORIAS, MATRIZ_ACORDES, RAIZES
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from _APP_.widgets.chord_diagram import ChordDiagram


class ChordsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._botoes_acordes = {}
        self._montar_ui()
        self.aplicar_tema(TEMA_PADRAO["cores"])

    def _montar_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            MARGEM_PAGINA, MARGEM_PAGINA // 2,
            MARGEM_PAGINA, MARGEM_PAGINA // 2,
        )
        layout.setSpacing(ESPACAMENTO_CARD)

        eyebrow = QLabel(TEXTOS_UI["acordes_selo"])
        eyebrow.setObjectName("eyebrow")
        title = QLabel(TEXTOS_UI["acordes_titulo"])
        title.setObjectName("pageTitle")
        description = QLabel(TEXTOS_UI["acordes_descricao"])
        description.setObjectName("bodyText")
        description.setWordWrap(True)
        layout.addWidget(eyebrow)
        layout.addWidget(title)
        layout.addWidget(description)

        notice = QFrame()
        notice.setObjectName("candidateNotice")
        notice_layout = QVBoxLayout(notice)
        notice_layout.setContentsMargins(
            PADDING_CARD, PADDING_CARD // 2,
            PADDING_CARD, PADDING_CARD // 2,
        )
        notice_layout.setSpacing(4)
        notice_title = QLabel(TEXTOS_UI["acordes_aviso_titulo"])
        notice_title.setObjectName("candidateNoticeTitle")
        notice_text = QLabel(TEXTOS_UI["acordes_aviso_texto"])
        notice_text.setObjectName("candidateNoticeBody")
        notice_text.setWordWrap(True)
        notice_layout.addWidget(notice_title)
        notice_layout.addWidget(notice_text)
        layout.addWidget(notice)

        columns = QHBoxLayout()
        columns.setSpacing(ESPACAMENTO_CARD)
        columns.addWidget(self._matriz_card(), stretch=6)
        columns.addWidget(self._detalhe_card(), stretch=4)
        layout.addLayout(columns, stretch=1)
        self._mostrar_acorde(MATRIZ_ACORDES[("C", "maior")])

    def _matriz_card(self):
        card = QFrame()
        card.setObjectName("surfaceCard")
        card.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        layout = QVBoxLayout(card)
        layout.setContentsMargins(
            PADDING_CARD, PADDING_CARD, PADDING_CARD, PADDING_CARD
        )
        layout.setSpacing(ESPACAMENTO_CARD // 2)

        title = QLabel(TEXTOS_UI["acordes_matriz_titulo"])
        title.setObjectName("sectionTitle")
        instruction = QLabel(TEXTOS_UI["acordes_matriz_instrucao"])
        instruction.setObjectName("mutedText")
        instruction.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(instruction)

        scroll = QScrollArea()
        scroll.setObjectName("chordMatrixScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        grid_content = QWidget()
        grid_content.setObjectName("chordMatrixContent")
        grid = QGridLayout(grid_content)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setHorizontalSpacing(5)
        grid.setVerticalSpacing(8)
        grid.setColumnMinimumWidth(0, 132)

        corner = QLabel(TEXTOS_UI["acordes_coluna_fundamental"])
        corner.setObjectName("matrixRowHeader")
        corner.setWordWrap(True)
        grid.addWidget(corner, 0, 0)

        for column, raiz in enumerate(RAIZES, start=1):
            header = QLabel(f"{raiz['nome']}\n{raiz['cifra']}")
            header.setObjectName("matrixColumnHeader")
            header.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header.setFixedSize(54, 42)
            grid.addWidget(header, 0, column)

        self._grupo_botoes = QButtonGroup(self)
        self._grupo_botoes.setExclusive(True)
        for row, categoria in enumerate(CATEGORIAS, start=1):
            row_label = QLabel(self._nome_linha(categoria["chave"]))
            row_label.setObjectName("matrixRowHeader")
            row_label.setWordWrap(True)
            row_label.setFixedWidth(132)
            grid.addWidget(
                row_label, row, 0,
                alignment=Qt.AlignmentFlag.AlignVCenter,
            )

            for column, raiz in enumerate(RAIZES, start=1):
                acorde = MATRIZ_ACORDES[(raiz["cifra"], categoria["chave"])]
                button = QPushButton(acorde["cifra"])
                button.setObjectName("chordMatrixButton")
                button.setCheckable(True)
                button.setFixedSize(54, 50)
                button.setCursor(Qt.CursorShape.PointingHandCursor)
                button.setAccessibleName(
                    f"{acorde['cifra']}, {acorde['nome']}, posição candidata"
                )
                button.setToolTip(
                    f"{acorde['nome']} — posição candidata calculada. "
                    "Clique para ver o diagrama."
                )
                button.clicked.connect(
                    lambda checked=False, item=acorde: self._mostrar_acorde(item)
                )
                self._grupo_botoes.addButton(button)
                self._botoes_acordes[
                    (raiz["cifra"], categoria["chave"])
                ] = button
                grid.addWidget(button, row, column)

        grid_content.setMinimumWidth(550)
        scroll.setWidget(grid_content)
        layout.addWidget(scroll, stretch=1)
        return card

    def _detalhe_card(self):
        card = QFrame()
        card.setObjectName("surfaceCard")
        card.setMinimumWidth(320)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(
            PADDING_CARD // 2, PADDING_CARD // 2,
            PADDING_CARD // 2, PADDING_CARD // 2,
        )

        scroll = QScrollArea()
        scroll.setObjectName("chordDetailScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        content = QWidget()
        content.setObjectName("chordDetailContent")
        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(ESPACAMENTO_CARD // 2)

        self._status = QLabel()
        self._status.setObjectName("chordBadge")
        self._status.setWordWrap(True)
        self._symbol = QLabel()
        self._symbol.setObjectName("chordTitle")
        self._name = QLabel()
        self._name.setObjectName("sectionTitle")
        self._name.setWordWrap(True)
        self._name.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._category = QLabel()
        self._category.setObjectName("mutedText")
        self._category.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._diagram = ChordDiagram(
            MATRIZ_ACORDES[("C", "maior")], compact=True
        )
        legend = QLabel(TEXTOS_UI["acordes_diagrama_legenda"])
        legend.setObjectName("mutedText")
        legend.setWordWrap(True)

        self._afinação = QLabel()
        self._afinação.setObjectName("bodyText")
        self._casas = QLabel()
        self._casas.setObjectName("bodyText")
        self._dedos = QLabel()
        self._dedos.setObjectName("bodyText")
        notes_title = QLabel(TEXTOS_UI["acordes_notas_titulo"])
        notes_title.setObjectName("eyebrow")
        self._notas = QLabel()
        self._notas.setObjectName("bodyText")
        self._notas.setWordWrap(True)
        strings_title = QLabel(TEXTOS_UI["acordes_cordas_titulo"])
        strings_title.setObjectName("eyebrow")
        self._cordas_layout = QVBoxLayout()
        self._cordas_layout.setSpacing(4)
        self._corda_labels = []
        for _ in range(4):
            linha = QLabel()
            linha.setObjectName("bodyText")
            linha.setWordWrap(True)
            self._corda_labels.append(linha)
            self._cordas_layout.addWidget(linha)
        self._observacao = QLabel()
        self._observacao.setObjectName("mutedText")
        self._observacao.setWordWrap(True)

        layout.addWidget(self._status, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self._symbol)
        layout.addWidget(self._name)
        layout.addWidget(self._category)
        layout.addWidget(
            self._diagram, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        layout.addWidget(legend)
        layout.addWidget(self._afinação)
        layout.addWidget(self._casas)
        layout.addWidget(self._dedos)
        layout.addWidget(notes_title)
        layout.addWidget(self._notas)
        layout.addWidget(strings_title)
        layout.addLayout(self._cordas_layout)
        layout.addWidget(self._observacao)
        layout.addStretch(1)
        layout.activate()
        scroll.setWidget(content)
        card_layout.addWidget(scroll)
        self._detalhe_content = content
        self._detalhe_layout = layout
        return card

    @staticmethod
    def _nome_linha(chave):
        return {
            "maior": "Maior",
            "menor": "Menor",
            "sustenida": "Sustenida\n(maior, provisório)",
            "dominante7": "Dominante\ncom sétima",
        }[chave]

    @staticmethod
    def _nome_dedo(numero):
        return {
            0: "sem dedo",
            1: "indicador",
            2: "médio",
            3: "anelar",
            4: "mínimo",
        }[numero]

    def _mostrar_acorde(self, acorde):
        self._symbol.setText(acorde["cifra"])
        self._name.setText(acorde["nome"])
        self._category.setText(acorde["categoria_nome"])
        self._status.setText(TEXTOS_UI["acordes_status_candidata"])
        self._diagram.set_chord(acorde)
        self._afinação.setText(
            f"{TEXTOS_UI['acordes_afinação']} · "
            f"{' – '.join(acorde['afinação'])} (4ª → 1ª)"
        )
        self._casas.setText(
            f"{TEXTOS_UI['acordes_casas']} · "
            f"{' – '.join(str(casa) for casa in acorde['casas'])}"
        )
        dedos = [
            "solta" if dedo == 0 else str(dedo)
            for dedo in acorde["dedos"]
        ]
        self._dedos.setText(
            f"{TEXTOS_UI['acordes_dedos']} · {' – '.join(dedos)}"
        )
        self._notas.setText(" · ".join(acorde["notas_resultantes"]))

        for linha, corda in zip(self._corda_labels, acorde["cordas"]):
            posicao = (
                "corda solta" if corda["casa"] == 0
                else f"casa {corda['casa']}, dedo {corda['dedo']} "
                f"({self._nome_dedo(corda['dedo'])})"
            )
            nota_afinação = acorde["afinação"][4 - corda["numero"]]
            linha.setText(
                f"{corda['numero']}ª corda · {nota_afinação} · "
                f"{posicao} · soa {corda['nota']}"
            )

        self._observacao.setText(
            acorde["observação"] or acorde["status_detalhe"]
        )
        botao = self._botoes_acordes.get(
            (acorde["raiz"], acorde["categoria"])
        )
        if botao:
            botao.setChecked(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self._ajustar_altura_detalhes)

    def _ajustar_altura_detalhes(self):
        if not hasattr(self, "_detalhe_layout"):
            return
        layout = self._detalhe_layout
        layout.activate()
        altura = layout.sizeHint().height()
        if layout.hasHeightForWidth():
            altura = max(
                altura,
                layout.heightForWidth(self._detalhe_content.width()),
            )
        self._detalhe_content.setMinimumHeight(altura)

    def aplicar_tema(self, cores):
        self.setStyleSheet(
            f"""
            QFrame#candidateNotice {{
                background: {cores["badge"]};
                border: 1px solid {cores["badge_borda"]};
                border-radius: 10px;
            }}
            QLabel#candidateNoticeTitle {{
                color: {cores["texto"]};
                font-weight: 700;
            }}
            QLabel#candidateNoticeBody {{
                color: {cores["texto_secundario"]};
            }}
            QScrollArea#chordMatrixScrollArea,
            QScrollArea#chordMatrixScrollArea::viewport,
            QScrollArea#chordDetailScrollArea,
            QScrollArea#chordDetailScrollArea::viewport {{
                background: {cores["superficie"]};
                border: none;
            }}
            QWidget#chordMatrixContent,
            QWidget#chordDetailContent {{
                background: {cores["superficie"]};
            }}
            QLabel#matrixColumnHeader {{
                color: {cores["texto"]};
                font-weight: 700;
            }}
            QLabel#matrixRowHeader {{
                color: {cores["texto_secundario"]};
            }}
            QPushButton#chordMatrixButton {{
                color: {cores["texto"]};
                background: {cores["campo"]};
                border: 1px solid {cores["borda_controle"]};
                border-radius: 8px;
                font-weight: 700;
            }}
            QPushButton#chordMatrixButton:hover {{
                border-color: {cores["destaque"]};
                background: {cores["superficie"]};
            }}
            QPushButton#chordMatrixButton:checked {{
                color: {cores["texto_destaque"]};
                background: {cores["destaque"]};
                border-color: {cores["destaque"]};
            }}
            QPushButton#chordMatrixButton:focus {{
                border: 2px solid {cores["foco"]};
            }}
            """
        )
        self._diagram.aplicar_tema(cores)
