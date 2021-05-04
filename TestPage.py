
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from ui.src.utils.util import round_corners

path = 'ui/assets/icons/elephant.png'


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI()
        self.ui.setupUi(self)



class UI:
    def setupUi(self, MainWindow):
        MainWindow.resize(200, 200)
        # Size pilicy
        size_pp = QSizePolicy(QSizePolicy.Preferred,
                            QSizePolicy.Preferred)
        # Main Window
        size_policy = MainWindow.sizePolicy().hasHeightForWidth()
        size_pp.setHeightForWidth(size_policy)
        MainWindow.setSizePolicy(size_pp)
        self.central_widget = QWidget(MainWindow)
        self.v_central = QVBoxLayout(self.central_widget)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        # Background
        self.background = QWidget()
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(10, 10, 10, 10)
        self.h_bg.setSpacing(0)
        ######################
        self.stacked = QStackedWidget()
        # self.stacked.setFixedSize(200, 200)
        self.stacked.setContentsMargins(0, 0, 0, 0)
        self.avatar = QLabel()
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners(path))
        self.avatar_widget = QWidget()
        # self.avatar_widget.setFixedSize(200, 200)
        self.avatar_widget.setStyleSheet('background:transparent; border:2px solid green')
        self.avatar_layout = QVBoxLayout(self.avatar_widget)
        self.avatar_layout.addWidget(self.avatar)
        self.avatar_layout.setAlignment(Qt.AlignCenter)

        self.status = QLabel()
        self.status.setStyleSheet('background:green; border-radius:15; border:2px solid white')
        self.status.setFixedSize(30, 30)
        self.status_widget = QWidget()
        self.status_widget.setStyleSheet('background:transparent')
        self.status_layout = QVBoxLayout(self.status_widget)
        self.status_layout.addWidget(self.status)
        self.status_layout.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        # self.status.setStyle()
        # self.stacked.addWidget(self.status_widget)
        self.stacked.addWidget(self.avatar_widget)
        self.stacked.addWidget(self.status_widget)

        self.stacked.setCurrentIndex(1)
        
        self.avatar_widget.setVisible(True)
        # self.status_widget.setVisible(True)

        # self.avatar.setScaledContents(True)


        self.h_bg.addWidget(self.stacked)
        self.v_central.addWidget(self.background)

        # Init#####################
        MainWindow.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)