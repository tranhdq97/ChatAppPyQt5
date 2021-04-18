import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ui.src.views import MainUI


class MainController(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUI()
        self.ui.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)

        self.show()
