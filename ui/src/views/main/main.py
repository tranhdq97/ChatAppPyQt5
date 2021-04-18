from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ...utils.util import *
from ...config.config import *
from ui.src.utils.util import round_corners, set_icon


class MainUI(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1000, 600)
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
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(5)
        # Left bar
        self.leftbar = LeftBar()
        # Body
        self.body = Body()
        # Add to layout
        self.h_bg.addWidget(self.leftbar)
        self.h_bg.addWidget(self.body)
        self.v_central.addWidget(self.background)

        # 
        MainWindow.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class LeftBar(QWidget):
    def __init__(self):
        super().__init__()
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        # Background
        self.background = QWidget()
        self.background.setMaximumWidth(100)
        self.background.setStyleSheet('background: rgb(3, 18, 41)')
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.v_bg.setSpacing(0)
        self.v_bg.setAlignment(Qt.AlignHCenter)
        # User
        self.user_box = UserBox()
        # Navigation
        self.btn_chat = TabButton(Icon.messenger)
        self.btn_home = TabButton(Icon.cat, icon_rounded=True)
        # Add to layout
        self.add_tab(self.user_box)
        self.add_tab(self.btn_chat)
        self.add_tab(self.btn_home)

        self.v_bg.addStretch()
        self.v_central.addWidget(self.background)

    def add_tab(self, btn_tab):
        layout = QHBoxLayout()
        layout.addWidget(btn_tab)
        self.v_bg.addLayout(layout)


class Body(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background: rgb(230, 243, 255)')
        self.v_center = QVBoxLayout(self)
        self.v_center.setContentsMargins(0, 0, 0, 0)
        self.v_center.setSpacing(0)
        # Background
        self.background = QWidget()
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.v_bg.setSpacing(0)
        # Dummy
        self.lbl_dummy = QLabel('Nothing')
        self.lbl_dummy.setStyleSheet('background: transparent')
        # Add to layout
        self.v_bg.addWidget(self.lbl_dummy)
        self.v_center.addWidget(self.background)


class UserBox(QWidget):
    def __init__(self):
        super().__init__()
        # Size policy
        size_ff = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy = self.sizePolicy().hasHeightForWidth()
        size_ff.setHeightForWidth(size_policy)
        self.setSizePolicy(size_ff)
        self.v_user_box = QVBoxLayout(self)
        self.v_user_box.setSpacing(0)
        self.v_user_box.setAlignment(Qt.AlignCenter)
        # Avatar
        self.btn_avatar = QPushButton()
        self.btn_avatar.setMaximumSize(70, 70)
        self.btn_avatar.setFlat(True)
        rounded = round_corners(Icon.elephant)
        set_icon(self.btn_avatar, rounded)
        # Name
        self.lbl_user_name = QLabel('Tranh')
        self.lbl_user_name.setStyleSheet('color: white')
        self.lbl_user_name.setAlignment(Qt.AlignCenter)
        self.lbl_user_name.setFont(QFont('ubuntu', 15, QFont.Bold))
        # Add to layout
        self.v_user_box.addWidget(self.btn_avatar)
        self.v_user_box.addWidget(self.lbl_user_name)


class TabButton(QPushButton):
    """ Moves to tab related to button when clicked.

    Attributes:
        icon (str): the path of icon
    """
    def __init__(self, icon=None, icon_rounded=False):
        super().__init__()
        self.setFlat(True)
        self.setMinimumSize(100, 100)
        self.setMaximumSize(100, 100)

        if icon is not None:
            if icon_rounded:
                icon = round_corners(icon)
            set_icon(self, icon, margin=40)
