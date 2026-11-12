from _CONFIGURA_ import (
    COR_ACENTO,
    COR_BORDA_CLARA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
    DIAGRAMA_ALTURA,
    DIAGRAMA_LARGURA,
    DIAGRAMA_MARGEM_ESQUERDA,
    DIAGRAMA_NUMERO_CASAS,
    DIAGRAMA_PASSO_CASA,
    DIAGRAMA_PASSO_CORDA,
    DIAGRAMA_RAIO_CORDA_SOLTA,
    DIAGRAMA_RAIO_DEDO,
    DIAGRAMA_TOPO,
    FONTE_NOME_UI,
    TEMA_PADRAO,
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QWidget


class ChordDiagram(QWidget):
    """Desenha um diagrama com a 4ª corda à esquerda e a 1ª à direita."""

    def __init__(self, chord, parent=None, compact=False):
        super().__init__(parent)
        self._chord = chord
        self._compact = compact
        self._cores_tema = dict(TEMA_PADRAO["cores"])
        self.setMinimumSize(
            280 if compact else DIAGRAMA_LARGURA,
            320 if compact else DIAGRAMA_ALTURA,
        )
        self._atualizar_acessibilidade()

    def sizeHint(self):
        if self._compact:
            return QSize(280, 320)
        return QSize(DIAGRAMA_LARGURA, DIAGRAMA_ALTURA)

    def set_chord(self, chord):
        self._chord = chord
        self._atualizar_acessibilidade()
        self.update()

    def _atualizar_acessibilidade(self):
        self.setAccessibleName(
            f"Diagrama do acorde {self._chord['cifra']} — {self._chord['nome']}"
        )
        self.setAccessibleDescription(
            "As cordas aparecem da 4ª à esquerda para a 1ª à direita. "
            "Os números nos pontos indicam os dedos da mão esquerda."
        )

    def aplicar_tema(self, cores):
        self._cores_tema = dict(cores)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        if self._compact:
            scale = min(
                self.width() / DIAGRAMA_LARGURA,
                self.height() / DIAGRAMA_ALTURA,
            )
            painter.scale(scale, scale)
        cor_texto = self._cores_tema.get("texto", COR_TEXTO)
        cor_texto_secundario = self._cores_tema.get(
            "texto_secundario", COR_TEXTO_SECUNDARIO
        )
        cor_linha = self._cores_tema.get("borda_controle", COR_BORDA_CLARA)
        cor_destaque = self._cores_tema.get("destaque", COR_ACENTO)

        string_step = DIAGRAMA_PASSO_CORDA
        fret_step = DIAGRAMA_PASSO_CASA
        left = DIAGRAMA_MARGEM_ESQUERDA
        top = DIAGRAMA_TOPO
        right = left + string_step * 3
        bottom = top + fret_step * DIAGRAMA_NUMERO_CASAS

        painter.setFont(QFont(FONTE_NOME_UI, 9, QFont.Weight.DemiBold))
        painter.setPen(QColor(cor_texto_secundario))
        painter.drawText(
            0, DIAGRAMA_TOPO // 2,
            self.width(), DIAGRAMA_TOPO // 2,
            Qt.AlignmentFlag.AlignCenter,
            "4ª        3ª        2ª        1ª",
        )

        for index in range(4):
            x = left + string_step * index
            painter.setPen(QPen(QColor(cor_linha), 2))
            painter.drawLine(x, top, x, bottom)

        for fret in range(DIAGRAMA_NUMERO_CASAS + 1):
            y = top + fret_step * fret
            line_width = 4 if fret == 0 else 2
            painter.setPen(QPen(QColor(cor_linha), line_width))
            painter.drawLine(left, y, right, y)
            if fret:
                painter.setFont(QFont(FONTE_NOME_UI, 8))
                painter.setPen(QColor(cor_texto_secundario))
                painter.drawText(
                    8,
                    y - fret_step,
                    left - 18,
                    fret_step,
                    Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight,
                    str(fret),
                )

        painter.setFont(QFont(FONTE_NOME_UI, 9, QFont.Weight.DemiBold))
        painter.setPen(QColor(cor_texto_secundario))
        notes = [item["nota"] for item in self._chord["cordas"]]
        for index, note in enumerate(notes):
            x = left + string_step * index
            painter.drawText(
                x - string_step // 2,
                bottom + DIAGRAMA_PASSO_CASA // 5,
                string_step,
                DIAGRAMA_PASSO_CASA // 2,
                Qt.AlignmentFlag.AlignCenter,
                note,
            )

        for index, item in enumerate(self._chord["cordas"]):
            x = left + string_step * index
            fret = item["casa"]
            finger = item["dedo"]
            if fret == 0:
                radius = DIAGRAMA_RAIO_CORDA_SOLTA
                painter.setPen(QPen(QColor(cor_texto_secundario), 2))
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawEllipse(
                    x - radius, top - DIAGRAMA_TOPO // 3,
                    radius * 2, radius * 2,
                )
                continue

            y = top + fret_step * (fret - 0.5)
            radius = DIAGRAMA_RAIO_DEDO
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(cor_destaque))
            painter.drawEllipse(x - radius, int(y) - radius, radius * 2, radius * 2)
            painter.setPen(QColor(cor_texto))
            painter.setFont(QFont(FONTE_NOME_UI, 9, QFont.Weight.Bold))
            painter.drawText(
                x - radius, int(y) - radius, radius * 2, radius * 2,
                Qt.AlignmentFlag.AlignCenter, str(finger),
            )

        painter.end()
