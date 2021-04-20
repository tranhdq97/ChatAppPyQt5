import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ui.src.views import MainUI, TitleBar


class MainController(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self._btn_clicked_connect()
        self.show()

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

    ############################ Title bar ################################
    def _title_bar_close_btn_clicked(self):
        self.ui.title_bar.close_app()
    
    def _title_bar_minimize_btn_clicked(self):
        self.ui.title_bar.minimize()

    def _title_bar_maximize_btn_clicked(self):
        self.ui.title_bar.maximize()
