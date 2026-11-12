# _APP_/main_window.py
"""
MainWindow — Janela principal do projeto.

Responsabilidades:
  - Aplicar tema e estilo global (de _CONFIGURA_)
  - Restaurar e salvar geometria/estado via appdata
  - Conectar shutdown ao thread_manager
  - Montar a estrutura de painéis e widgets

Expanda este arquivo conforme o projeto crescer.
Painéis grandes devem ir para subpastas dentro de _APP_/.
"""

from _CONFIGURA_ import (
    TITULO_APP, VERSAO_APP,
    LARGURA_PADRAO, ALTURA_PADRAO,
    LARGURA_MIN, ALTURA_MIN,
    LARGURA_SIDEBAR, PADDING_CARD,
    CONFIG_TAMANHO_ICONE,
    IMAGEM_ICO,
    TEXTOS_UI,
    TEXTOS_CONFIGURACOES,
    estilos_para_tema,
)
from _LOGS_ import log
from _APPDATA_ import appdata
from _THREADS_ import thread_manager
from PySide6.QtCore import Qt, QByteArray, QSize
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from _APP_.pages.chords_page import ChordsPage
from _APP_.pages.home_page import HomePage
from _APP_.pages.learning_page import LearningPage
from _APP_.settings_dialog import SettingsDialog
from _UTILIDADES_.icones import ico_config


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("MainWindow", "__init__", "inicializando janela principal...")

        self._tema = appdata.ler_tema()
        self._configurar_janela()
        self._aplicar_estilo()
        self._montar_ui()
        self._restaurar_sessao()
        self._conectar_shutdown()

        log.ok("MainWindow", "__init__", "janela principal pronta")

    # ── Configuração ─────────────────────────────────────────────────────────

    def _configurar_janela(self):
        self.setWindowTitle(f"{TITULO_APP} {VERSAO_APP}")
        self.setMinimumSize(LARGURA_MIN, ALTURA_MIN)
        self.resize(LARGURA_PADRAO, ALTURA_PADRAO)

        # Ícone da janela
        import os
        if os.path.isfile(IMAGEM_ICO):
            from PySide6.QtGui import QIcon
            self.setWindowIcon(QIcon(IMAGEM_ICO))

    def _aplicar_estilo(self):
        self.setStyleSheet(estilos_para_tema(self._tema))
        if hasattr(self, "_botao_config"):
            self._botao_config.setIcon(
                ico_config(self._tema["cores"]["texto_menu"])
            )
        if hasattr(self, "_chords_page"):
            self._chords_page.aplicar_tema(self._tema["cores"])

    # ── UI ───────────────────────────────────────────────────────────────────

    def _montar_ui(self):
        central = QWidget()
        central.setObjectName("appCanvas")
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("appSidebar")
        sidebar.setFixedWidth(LARGURA_SIDEBAR)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(
            PADDING_CARD, PADDING_CARD * 2, PADDING_CARD, PADDING_CARD
        )
        sidebar_layout.setSpacing(PADDING_CARD // 2)

        brand = QLabel(TEXTOS_UI["marca"])
        brand.setObjectName("brandTitle")
        subtitle = QLabel(TEXTOS_UI["submarca"])
        subtitle.setObjectName("brandSubtitle")
        sidebar_layout.addWidget(brand)
        sidebar_layout.addWidget(subtitle)
        sidebar_layout.addSpacing(PADDING_CARD * 2)

        self._nav_inicio = self._criar_botao_nav(TEXTOS_UI["nav_inicio"])
        self._nav_trilha = self._criar_botao_nav(TEXTOS_UI["nav_trilha"])
        self._nav_acordes = self._criar_botao_nav(TEXTOS_UI["nav_acordes"])
        self._nav_inicio.clicked.connect(self._mostrar_inicio)
        self._nav_trilha.clicked.connect(self._mostrar_trilha)
        self._nav_acordes.clicked.connect(self._mostrar_acordes)
        sidebar_layout.addWidget(self._nav_inicio)
        sidebar_layout.addWidget(self._nav_trilha)
        sidebar_layout.addWidget(self._nav_acordes)

        self._botao_config = QPushButton(TEXTOS_UI["nav_config"])
        self._botao_config.setObjectName("settingsButton")
        self._botao_config.setIcon(
            ico_config(self._tema["cores"]["texto_menu"])
        )
        self._botao_config.setIconSize(
            QSize(CONFIG_TAMANHO_ICONE, CONFIG_TAMANHO_ICONE)
        )
        self._botao_config.setCursor(Qt.CursorShape.PointingHandCursor)
        self._botao_config.setToolTip(TEXTOS_CONFIGURACOES["tooltip"])
        self._botao_config.clicked.connect(self._abrir_configuracoes)
        sidebar_layout.addWidget(self._botao_config)
        sidebar_layout.addStretch(1)

        tuning = QLabel(TEXTOS_UI["rodape_afinação"])
        tuning.setObjectName("sidebarFooter")
        tuning.setWordWrap(True)
        sidebar_layout.addWidget(tuning)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        header = QFrame()
        header.setObjectName("contentHeader")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(
            PADDING_CARD * 2, PADDING_CARD, PADDING_CARD * 2, PADDING_CARD
        )
        header_label = QLabel(TEXTOS_UI["header_titulo"])
        header_label.setObjectName("mutedText")
        header_layout.addWidget(header_label)
        header_layout.addStretch(1)

        self._pages = QStackedWidget()
        self._home_page = HomePage()
        self._learning_page = LearningPage()
        self._chords_page = ChordsPage()
        self._chords_page.aplicar_tema(self._tema["cores"])
        self._pages.addWidget(self._home_page)
        self._pages.addWidget(self._learning_page)
        self._pages.addWidget(self._chords_page)
        self._home_page.abrir_trilha.connect(self._mostrar_trilha)
        self._home_page.abrir_acordes.connect(self._mostrar_acordes)

        content_layout.addWidget(header)
        content_layout.addWidget(self._pages, stretch=1)
        root.addWidget(sidebar)
        root.addWidget(content, stretch=1)

        # Abra diretamente no conteúdo que o aluno procura; a Home continua
        # acessível pela navegação lateral.
        self._selecionar_pagina(2)
        self.statusBar().showMessage(TEXTOS_UI["status_pronto"])

        log.ok("MainWindow", "_montar_ui", "UI montada")

    @staticmethod
    def _criar_botao_nav(texto):
        button = QPushButton(texto)
        button.setObjectName("navButton")
        button.setCheckable(True)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        return button

    def _selecionar_pagina(self, indice):
        self._pages.setCurrentIndex(indice)
        botoes = (self._nav_inicio, self._nav_trilha, self._nav_acordes)
        for botao_indice, botao in enumerate(botoes):
            botao.setChecked(botao_indice == indice)

    def _mostrar_inicio(self):
        self._selecionar_pagina(0)

    def _mostrar_trilha(self):
        self._selecionar_pagina(1)

    def _mostrar_acordes(self):
        self._selecionar_pagina(2)

    def _abrir_configuracoes(self):
        dialogo = SettingsDialog(self._tema, self)
        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return

        tema = dialogo.tema_selecionado
        if not appdata.salvar_tema(tema):
            QMessageBox.warning(
                self,
                TEXTOS_UI["nav_config"],
                TEXTOS_CONFIGURACOES["falha_salvar"],
            )
            return

        self._tema = tema
        self._aplicar_estilo()
        self.statusBar().showMessage(TEXTOS_CONFIGURACOES["salvo"])
        log.ok("MainWindow", "_abrir_configuracoes", "tema atualizado")

    # ── Sessão ───────────────────────────────────────────────────────────────

    def _restaurar_sessao(self):
        """Restaura geometria e estado salvos na sessão anterior."""
        sessao = appdata.ler_sessao()
        try:
            if "geometria" in sessao:
                self.restoreGeometry(QByteArray.fromBase64(
                    sessao["geometria"].encode()
                ))
            if "estado" in sessao:
                self.restoreState(QByteArray.fromBase64(
                    sessao["estado"].encode()
                ))
            log.ok("MainWindow", "_restaurar_sessao", "sessão restaurada")
        except Exception as e:
            log.aviso("MainWindow", "_restaurar_sessao", f"falha ao restaurar sessão: {e}")

    def _salvar_sessao(self):
        """Salva geometria e estado atual para a próxima sessão."""
        try:
            sessao = {
                "geometria": self.saveGeometry().toBase64().data().decode(),
                "estado":    self.saveState().toBase64().data().decode(),
            }
            appdata.salvar_sessao(sessao)
        except Exception as e:
            log.erro("MainWindow", "_salvar_sessao", f"falha ao salvar sessão: {e}")

    # ── Shutdown ─────────────────────────────────────────────────────────────

    def _conectar_shutdown(self):
        """Conecta encerramento ordenado ao sinal aboutToQuit."""
        from PySide6.QtWidgets import QApplication
        app = QApplication.instance()
        if app:
            app.aboutToQuit.connect(self._ao_encerrar)

    def _ao_encerrar(self):
        log.info("MainWindow", "_ao_encerrar", "encerrando aplicação...")
        thread_manager.encerrar_todas()
        log.info("MainWindow", "_ao_encerrar", "shutdown concluído")

    def closeEvent(self, event):
        log.info("MainWindow", "closeEvent", "janela fechando...")
        self._salvar_sessao()
        super().closeEvent(event)
