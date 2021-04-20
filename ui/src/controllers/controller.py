import time
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
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

        self._btn_clicked_connect()
        self.show()


    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize
        )
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

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

    ############################ Title bar ################################
    def _title_bar_close_btn_clicked(self):
        self.ui.title_bar.close_app()
    
    def _title_bar_minimize_btn_clicked(self):
        self.ui.title_bar.minimize()

    def _title_bar_maximize_btn_clicked(self):
        self.ui.title_bar.maximize()

    def _title_bar_restore_btn_clicked(self):
        self.ui.title_bar.restore()
