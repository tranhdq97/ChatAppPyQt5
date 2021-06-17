from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QMetaObject
from ..views.main import InfoPage


class MainController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = InfoPage()


        self.setCentralWidget(self.ui)
        QMetaObject.connectSlotsByName(self)