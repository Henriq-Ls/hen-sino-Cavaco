# _UTILIDADES_/icones.py
"""
Centraliza todos os ícones do projeto.

Usa qtawesome como fonte principal.
Se qtawesome não estiver instalado, retorna QIcon vazio silenciosamente.

Uso:
    from _UTILIDADES_.icones import icone, icone_colorido

    btn.setIcon(icone("fa5s.folder-open"))
    btn.setIcon(icone_colorido("fa5s.save", "#3a7bd5"))

Referência de ícones: https://fontawesome.com/icons (prefixo fa5s, fa5r, fa5b, mdi, ei)
"""

import math

from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QIcon, QColor, QPainter, QPen, QPixmap
from _CONFIGURA_ import COR_TEXTO, COR_ACENTO, COR_PERIGO, COR_SUCESSO


def icone(nome: str, cor: str = COR_TEXTO) -> QIcon:
    """
    Retorna um QIcon do qtawesome.
    Se qtawesome não estiver disponível, retorna QIcon vazio.

    Args:
        nome: nome do ícone (ex: "fa5s.folder-open", "mdi.content-save")
        cor:  cor hexadecimal (padrão: COR_TEXTO do _CONFIGURA_)
    """
    try:
        import qtawesome as qta
        return qta.icon(nome, color=cor)
    except Exception:
        return _icone_basico(nome, cor)


def _icone_basico(nome: str, cor: str) -> QIcon:
    """Desenha os ícones essenciais quando qtawesome não estiver instalado."""
    if nome not in ("fa5s.cog", "fa5s.palette"):
        return QIcon()

    imagem = QPixmap(64, 64)
    imagem.fill(Qt.GlobalColor.transparent)
    painter = QPainter(imagem)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    painter.setPen(QPen(QColor(cor), 6, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(Qt.BrushStyle.NoBrush)

    if nome == "fa5s.cog":
        centro = QPointF(32, 32)
        for angulo in range(0, 360, 45):
            rad = math.radians(angulo)
            inicio = QPointF(
                centro.x() + math.cos(rad) * 18,
                centro.y() + math.sin(rad) * 18,
            )
            fim = QPointF(
                centro.x() + math.cos(rad) * 27,
                centro.y() + math.sin(rad) * 27,
            )
            painter.drawLine(inicio, fim)
        painter.drawEllipse(QRectF(15, 15, 34, 34))
        painter.drawEllipse(QRectF(27, 27, 10, 10))
    else:
        painter.drawEllipse(QRectF(9, 13, 46, 40))
        painter.setBrush(QColor(cor))
        for x, y in ((22, 27), (34, 23), (44, 32), (31, 40)):
            painter.drawEllipse(QRectF(x, y, 5, 5))

    painter.end()
    return QIcon(imagem)


def icone_colorido(nome: str, cor: str) -> QIcon:
    """Ícone com cor específica."""
    return icone(nome, cor)


# ── Ícones pré-definidos (expanda conforme o projeto) ────────────────────────
# Importe estes em vez de escrever strings de ícone espalhadas pelo código.

def ico_salvar()    -> QIcon: return icone("fa5s.save",         COR_ACENTO)
def ico_abrir()     -> QIcon: return icone("fa5s.folder-open",  COR_ACENTO)
def ico_novo()      -> QIcon: return icone("fa5s.file",         COR_ACENTO)
def ico_fechar()    -> QIcon: return icone("fa5s.times",        COR_TEXTO)
def ico_config(cor: str = COR_TEXTO) -> QIcon:
    return icone("fa5s.cog", cor)
def ico_paleta(cor: str = COR_ACENTO) -> QIcon:
    return icone("fa5s.palette", cor)
def ico_info()      -> QIcon: return icone("fa5s.info-circle",  COR_ACENTO)
def ico_aviso()     -> QIcon: return icone("fa5s.exclamation-triangle", "#FFC107")
def ico_erro()      -> QIcon: return icone("fa5s.times-circle", COR_PERIGO)
def ico_ok()        -> QIcon: return icone("fa5s.check-circle", COR_SUCESSO)
def ico_atualizar() -> QIcon: return icone("fa5s.sync-alt",     COR_TEXTO)
def ico_buscar()    -> QIcon: return icone("fa5s.search",       COR_TEXTO)
def ico_lixo()      -> QIcon: return icone("fa5s.trash-alt",    COR_PERIGO)
def ico_adicionar() -> QIcon: return icone("fa5s.plus",         COR_SUCESSO)
def ico_voltar()    -> QIcon: return icone("fa5s.arrow-left",   COR_TEXTO)
def ico_avancar()   -> QIcon: return icone("fa5s.arrow-right",  COR_TEXTO)
def ico_subir()     -> QIcon: return icone("fa5s.arrow-up",     COR_TEXTO)
def ico_inicio()    -> QIcon: return icone("fa5s.home",         COR_TEXTO)
def ico_nova_pasta()-> QIcon: return icone("fa5s.folder-plus",  COR_ACENTO)
def ico_copiar()    -> QIcon: return icone("fa5s.copy",         COR_TEXTO)
def ico_renomear()  -> QIcon: return icone("fa5s.edit",         COR_TEXTO)
