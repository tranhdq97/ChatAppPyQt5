from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QStackedWidget, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from ...utils.util import *
from ...configs.config import *
from ui.src.utils.util import round_corners, set_icon
from ..title_bar.title_bar import TitleBar
from . import *


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
        self.h_bg.setSpacing(0)
        # Title bar
        self.title_bar = TitleBar(MainWindow)
        self.pressing = False
        # Left bar
        self.left_bar = LeftBar()
        # Body
        self.body = Body()
        # Add to layout
        self.h_bg.addWidget(self.left_bar)
        self.h_bg.addWidget(self.body)
        self.v_central.addWidget(self.title_bar)
        self.v_central.addWidget(self.background)
        # Init
        self._add_tabs()
        MainWindow.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _add_tabs(self):
        self.chat_page = ChatPage(Tab.chat)
        self._add_single_tab(TabWidget(
            self.chat_page, Icon.chat, icon_rounded=False, chosen=True))
        self.home_page = HomePage(Tab.home)
        self._add_single_tab(TabWidget(
            self.home_page, Icon.home, icon_rounded=True))
        # Set default tab
        self.left_bar.v_bg.addStretch()
        self.body.add(page=self.chat_page)

    def _add_single_tab(self, tab):
        self.left_bar.add_tab(tab)

    def set_default(self):
        """ Defaults left bar and body.
        """
        pass


class LeftBar(QWidget):
    def __init__(self):
        super().__init__()
        # size policy
        size_fp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        policy = self.sizePolicy().hasHeightForWidth()
        size_fp.setHeightForWidth(policy)
        self.setSizePolicy(size_fp)
        self.setStyleSheet('background: rgb(3, 18, 41)')
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        # Background
        self.background = QWidget()
        self.background.setMaximumWidth(90)
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.v_bg.setSpacing(0)
        self.v_bg.setAlignment(Qt.AlignHCenter)
        # User
        self.user_box = UserBox()
        # Tabs
        self._tabs = []
        # Add to layouts
        self.v_bg.addWidget(self.user_box)
        self.v_central.addWidget(self.background)

    def add_tab(self, tab):
        self._tabs.append(tab)
        self.v_bg.addWidget(tab)

    @property
    def current_tab(self):
        return TabWidget.current_tab
    
    @property
    def tabs(self):
        return self._tabs


class Body(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background: rgb(230, 243, 255)')

    def add(self, page):
        """ Adds new widget into the stacked widget and shows this page.

        Args:
            page (QWidget): the added page
        """
        index = self.addWidget(page)
        self.setCurrentIndex(index)

    def remove(self, page):
        """ Removes page out of the stacked widget.

        Args:
            page (QWidget): the removed page
        """
        self.removeWidget(page)


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

    def update(self):
        pass

    def update_status(status):
        pass


class TabWidget(QWidget):
    """ Moves to tab related to button when clicked.

    Attributes:
        icon (str): the path of icon
    """
    current_tab = None

    def __init__(self, page, icon=None, icon_rounded=False, chosen=False):
        super().__init__()
        self.setObjectName(page.name)
        self._page = page
        self._chosen_bg_style = Style.Tab.chosen_bg
        self.v_central = QVBoxLayout(self)
        self.v_central.setSpacing(0)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        # Background
        self.background = QWidget()
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setAlignment(Qt.AlignCenter)
        self.h_bg.setContentsMargins(10, 10, 10, 10)
        # Button
        self.btn = QPushButton()
        self.btn.setFlat(True)
        self.set_size((60, 60))
        # Add to layout
        self.h_bg.addWidget(self.btn)
        self.v_central.addWidget(self.background)

        if chosen:
            TabWidget.current_tab = self
            self.setStyleSheet(self._chosen_bg_style)

        if icon is not None:
            if icon_rounded:
                icon = round_corners(icon)
            set_icon(self.btn, icon, margin=20)


    def set_size(self, size):
        self.btn.setFixedSize(*size)

    def select(self):
        TabWidget.current_tab.unselect()
        self.setStyleSheet(self._chosen_bg_style)
        TabWidget.current_tab = self

    def unselect(self):
        self.setStyleSheet('background:transparent')

    def update_theme(self):
        pass

    @property
    def name(self):
        return self.objectName()

    @property
    def page(self):
        return self._page



    
