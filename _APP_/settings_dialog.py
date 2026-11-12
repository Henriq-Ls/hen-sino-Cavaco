"""Diálogo para escolher e pré-visualizar as cores do aplicativo."""

from copy import deepcopy

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QComboBox,
    QColorDialog,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from _CONFIGURA_ import (
    CONFIG_ALTURA_DIALOGO,
    CONFIG_ALTURA_MIN_DIALOGO,
    CONFIG_ESPACAMENTO,
    CONFIG_LARGURA_DIALOGO,
    CONFIG_LARGURA_MIN_DIALOGO,
    CONFIG_TAMANHO_AMOSTRA,
    CONFIG_TAMANHO_ICONE,
    CORES_TEMA_EDITAVEIS,
    TEMAS_PREDEFINIDOS,
    TEMA_PADRAO,
    TEXTOS_CONFIGURACOES,
    criar_tema_personalizado,
    normalizar_tema,
)
from _UTILIDADES_.icones import ico_paleta


class SettingsDialog(QDialog):
    """Escolha uma paleta pronta ou personalize cinco cores principais."""

    def __init__(self, tema_atual=None, parent=None):
        super().__init__(parent)
        self.setObjectName("settingsDialog")
        self.setWindowTitle(TEXTOS_CONFIGURACOES["titulo"])
        self.setModal(True)
        self.resize(CONFIG_LARGURA_DIALOGO, CONFIG_ALTURA_DIALOGO)
        self.setMinimumSize(
            CONFIG_LARGURA_MIN_DIALOGO,
            CONFIG_ALTURA_MIN_DIALOGO,
        )

        self._tema = normalizar_tema(tema_atual or TEMA_PADRAO)
        self._preset = self._tema["preset"]
        self._cores = deepcopy(self._tema["cores"])
        self._amostras = {}
        self._botoes_cor = {}
        self._montar_ui()
        self._atualizar_previa()

    @property
    def tema_selecionado(self):
        return normalizar_tema({
            "versao": 1,
            "preset": self._preset,
            "cores": self._cores,
        })

    def _montar_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            CONFIG_ESPACAMENTO * 2,
            CONFIG_ESPACAMENTO * 2,
            CONFIG_ESPACAMENTO * 2,
            CONFIG_ESPACAMENTO,
        )
        layout.setSpacing(CONFIG_ESPACAMENTO)

        title = QLabel(TEXTOS_CONFIGURACOES["titulo"])
        title.setObjectName("pageTitle")
        description = QLabel(TEXTOS_CONFIGURACOES["descricao"])
        description.setObjectName("bodyText")
        description.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(description)

        preset_label = QLabel(TEXTOS_CONFIGURACOES["seletor_tema"])
        preset_label.setObjectName("sectionTitle")
        self._preset_combo = QComboBox()
        self._preset_combo.setObjectName("themePresetCombo")
        self._preset_combo.setAccessibleName(
            TEXTOS_CONFIGURACOES["seletor_tema"]
        )
        for preset_id, preset in TEMAS_PREDEFINIDOS.items():
            self._preset_combo.addItem(preset["nome"], preset_id)
        self._preset_combo.addItem(
            TEXTOS_CONFIGURACOES["personalizado"], "personalizado"
        )
        combo_row = QHBoxLayout()
        combo_row.addWidget(preset_label)
        combo_row.addWidget(self._preset_combo, stretch=1)
        layout.addLayout(combo_row)

        scroll = QScrollArea()
        scroll.setObjectName("settingsScrollArea")
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setWidgetResizable(True)
        content = QWidget()
        content.setObjectName("settingsContent")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(CONFIG_ESPACAMENTO)

        colors_title = QLabel(TEXTOS_CONFIGURACOES["cores_principais"])
        colors_title.setObjectName("sectionTitle")
        content_layout.addWidget(colors_title)

        for color_key, label_text in CORES_TEMA_EDITAVEIS:
            row = QHBoxLayout()
            row.setSpacing(CONFIG_ESPACAMENTO)
            label = QLabel(label_text)
            label.setMinimumWidth(190)
            sample = QFrame()
            sample.setObjectName("settingsSwatch")
            sample.setFixedSize(
                CONFIG_TAMANHO_AMOSTRA, CONFIG_TAMANHO_AMOSTRA
            )
            button = QPushButton(TEXTOS_CONFIGURACOES["escolher_cor"])
            button.setObjectName("settingsColorButton")
            button.setIcon(ico_paleta(self._cores["destaque"]))
            button.setIconSize(QSize(CONFIG_TAMANHO_ICONE, CONFIG_TAMANHO_ICONE))
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(
                lambda checked=False, key=color_key: self._escolher_cor(key)
            )
            row.addWidget(label, stretch=1)
            row.addWidget(sample)
            row.addWidget(button)
            content_layout.addLayout(row)
            self._amostras[color_key] = sample
            self._botoes_cor[color_key] = button

        self._aviso_contraste = QLabel()
        self._aviso_contraste.setObjectName("settingsWarning")
        self._aviso_contraste.setWordWrap(True)
        content_layout.addWidget(self._aviso_contraste)

        preview_title = QLabel(TEXTOS_CONFIGURACOES["previa"])
        preview_title.setObjectName("sectionTitle")
        content_layout.addWidget(preview_title)

        self._preview = QFrame()
        self._preview.setObjectName("themePreview")
        preview_layout = QHBoxLayout(self._preview)
        preview_layout.setContentsMargins(
            CONFIG_ESPACAMENTO,
            CONFIG_ESPACAMENTO,
            CONFIG_ESPACAMENTO,
            CONFIG_ESPACAMENTO,
        )
        sample_text = QVBoxLayout()
        self._preview_heading = QLabel(TEXTOS_CONFIGURACOES["previa_titulo"])
        self._preview_heading.setObjectName("sectionTitle")
        self._preview_body = QLabel(TEXTOS_CONFIGURACOES["previa_texto"])
        self._preview_body.setObjectName("bodyText")
        self._preview_body.setWordWrap(True)
        sample_text.addWidget(self._preview_heading)
        sample_text.addWidget(self._preview_body)
        preview_layout.addLayout(sample_text, stretch=1)
        self._preview_button = QPushButton(TEXTOS_CONFIGURACOES["aplicar"])
        self._preview_button.setObjectName("themePreviewPrimaryButton")
        self._preview_button.setIcon(ico_paleta(self._cores["destaque"]))
        self._preview_button.setIconSize(
            QSize(CONFIG_TAMANHO_ICONE, CONFIG_TAMANHO_ICONE)
        )
        preview_layout.addWidget(self._preview_button)
        content_layout.addWidget(self._preview)
        content_layout.addStretch(1)
        scroll.setWidget(content)
        layout.addWidget(scroll, stretch=1)

        buttons = QHBoxLayout()
        restore = QPushButton(TEXTOS_CONFIGURACOES["restaurar"])
        restore.setObjectName("settingsRestoreButton")
        restore.setIcon(ico_paleta(self._cores["destaque"]))
        restore.clicked.connect(self._restaurar_inicial)
        buttons.addWidget(restore)
        buttons.addStretch(1)

        cancel = QPushButton(TEXTOS_CONFIGURACOES["cancelar"])
        cancel.setObjectName("settingsCancelButton")
        cancel.clicked.connect(self.reject)
        apply = QPushButton(TEXTOS_CONFIGURACOES["aplicar"])
        apply.setObjectName("settingsApplyButton")
        apply.setIcon(ico_paleta(self._cores["texto_destaque"]))
        apply.setDefault(True)
        apply.clicked.connect(self.accept)
        buttons.addWidget(cancel)
        buttons.addWidget(apply)
        layout.addLayout(buttons)

        self._preset_combo.currentIndexChanged.connect(
            self._selecionar_preset
        )
        self._selecionar_preset_inicial()

    def _selecionar_preset_inicial(self):
        index = self._preset_combo.findData(self._preset)
        if index < 0:
            index = self._preset_combo.findData("personalizado")
            self._preset = "personalizado"
        self._preset_combo.setCurrentIndex(index)

    def _selecionar_preset(self, _index):
        preset = self._preset_combo.currentData()
        if preset == "personalizado":
            self._preset = preset
        else:
            self._preset = preset
            self._cores = deepcopy(TEMAS_PREDEFINIDOS[preset]["cores"])
        self._atualizar_previa()

    def _escolher_cor(self, chave):
        dialogo = QColorDialog(
            QColor(self._cores[chave]),
            self,
        )
        dialogo.setWindowTitle(
            f'{TEXTOS_CONFIGURACOES["escolher_cor"]} — '
            f'{dict(CORES_TEMA_EDITAVEIS)[chave]}'
        )
        dialogo.setOption(QColorDialog.ColorDialogOption.ShowAlphaChannel, False)
        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return

        cor = dialogo.selectedColor()
        if not cor.isValid():
            return
        cores_base = {
            key: self._cores[key]
            for key, _label in CORES_TEMA_EDITAVEIS
        }
        cores_base[chave] = cor.name().upper()
        self._tema = criar_tema_personalizado(cores_base)
        self._preset = "personalizado"
        self._cores = deepcopy(self._tema["cores"])
        self._selecionar_preset_inicial()
        self._atualizar_previa()

    def _restaurar_inicial(self):
        self._tema = normalizar_tema(TEMA_PADRAO)
        self._preset = self._tema["preset"]
        self._cores = deepcopy(self._tema["cores"])
        self._selecionar_preset_inicial()
        self._atualizar_previa()

    def _atualizar_previa(self):
        cores = self._cores
        for chave, sample in self._amostras.items():
            sample.setStyleSheet(
                "QFrame#settingsSwatch {"
                f"background: {cores[chave]};"
                f"border: 1px solid {cores['borda_controle']};"
                "border-radius: 6px;"
                "}"
            )
        for button in self._botoes_cor.values():
            button.setIcon(ico_paleta(cores["destaque"]))

        self._preview.setStyleSheet(
            "QFrame#themePreview {"
            f"background: {cores['superficie']};"
            f"border: 1px solid {cores['borda']};"
            "border-radius: 12px;"
            "}"
        )
        self._preview_heading.setStyleSheet(
            f"color: {cores['texto']}; background: transparent;"
        )
        self._preview_body.setStyleSheet(
            f"color: {cores['texto_secundario']}; background: transparent;"
        )
        self._preview_button.setStyleSheet(
            "QPushButton#themePreviewPrimaryButton {"
            f"background: {cores['destaque']};"
            f"color: {cores['texto_destaque']};"
            "border: none; border-radius: 8px; padding: 9px 16px;"
            "font-weight: 700;"
            "}"
        )
        self._preview_button.setIcon(ico_paleta(cores["texto_destaque"]))

        contraste = self._contraste(cores["texto"], cores["fundo"])
        if contraste < 4.5:
            self._aviso_contraste.setText(
                TEXTOS_CONFIGURACOES["aviso_contraste"]
            )
        else:
            self._aviso_contraste.clear()

    @staticmethod
    def _contraste(cor_a, cor_b):
        def luminancia(cor):
            canais = []
            for valor in QColor(cor).getRgb()[:3]:
                normalizado = valor / 255
                canais.append(
                    normalizado / 12.92 if normalizado <= 0.04045
                    else ((normalizado + 0.055) / 1.055) ** 2.4
                )
            return (
                0.2126 * canais[0]
                + 0.7152 * canais[1]
                + 0.0722 * canais[2]
            )

        valores = sorted((luminancia(cor_a), luminancia(cor_b)))
        return (valores[1] + 0.05) / (valores[0] + 0.05)
