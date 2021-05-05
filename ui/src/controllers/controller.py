import time
import random
from PyQt5.QtWidgets import QMainWindow, QSizeGrip
from PyQt5.QtCore import Qt
from ui.src.views import MainUI, TitleBar


class MainController(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.gripSize = 16
        self.grips = []
        # Resize window
        for i in range(4):
            grip = QSizeGrip(self)
            grip.setVisible(False)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

        self._btn_clicked_connect()

    ############################# Signals #############################

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize
        )
        self.grips[2].setVisible(True)

    def _btn_clicked_connect(self):
        self.ui.title_bar.btn_close.clicked.connect(
            self._title_bar_close_btn_clicked
        )
        self.ui.title_bar.btn_max.clicked.connect(
            self._title_bar_maximize_btn_clicked
        )
        self.ui.title_bar.btn_min.clicked.connect(
            self._title_bar_minimize_btn_clicked
        )
        self.ui.title_bar.btn_restore.clicked.connect(
            self._title_bar_restore_btn_clicked
        )
        self.ui.chat_page.top.search_box.contacts.clicked.connect(
            self._chat_page_contacts_btn_clicked
        )
        self.ui.chat_page.body.conversation.msg_entry.send_btn.clicked.connect(
            self._chat_page_send_btn_clicked
        )
        for tab in self.ui.left_bar.tabs:
            tab.btn.clicked.connect(
                lambda checked, t=tab : self._choose_tab(t)
            )

    #########################################################################
    ######################## Manipulating Funcs #############################

    def _navigate(self, page=None):
        self.ui.body.add(page)

    def _remove(self, page=None):
        pass

    ############################ Title bar ##################################

    def _title_bar_close_btn_clicked(self):
        self.ui.title_bar.close_app()
    
    def _title_bar_minimize_btn_clicked(self):
        self.ui.title_bar.minimize()

    def _title_bar_maximize_btn_clicked(self):
        self.ui.title_bar.maximize()

    def _title_bar_restore_btn_clicked(self):
        self.ui.title_bar.restore()

    ############################ LeftBar ###############################

    def _choose_tab(self, tab):
        tab.select()
        self._navigate(tab.page)

    ############################# Pages ################################
    # Chat page

    def _chat_page_contacts_btn_clicked(self):
        self.ui.chat_page.body.history.switch(
            self.ui.chat_page.top.search_box.on_contacts)
        self.ui.chat_page.top.search_box.switch_contacts()

    def _chat_page_send_btn_clicked(self):
        content = self.ui.chat_page.body.conversation.msg_entry.content
        if content != "":
            if random.random() > 0.5:
                self.ui.chat_page.body.conversation.send(content)
            else:
                self.ui.chat_page.body.conversation.receive(content)

