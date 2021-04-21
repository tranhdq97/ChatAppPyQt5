from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QScrollArea, QSizePolicy, QVBoxLayout, QWidget
from ..base_page import BasePage, BaseWidget
from ....config.config import *
from ....utils.util import *


class ChatPage(BasePage):
    def __init__(self, name):
        super().__init__(name=name)
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.v_bg.setSpacing(0)
        # Top search
        self.top = Top()
        self.body = Body()
        # Add to layout
        self.v_bg.addWidget(self.top)
        self.v_bg.addWidget(self.body)

########################## Top ############################

class Top(BaseWidget):
    def __init__(self):
        super().__init__()
        # Size policy
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet('background:rgb(0, 37, 74)')
        # Background
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(0)
        self.search_box = SearchBox()
        self.info_box = InfoBox()
        # Add to layout
        self.h_bg.addWidget(self.search_box)
        self.h_bg.addWidget(self.info_box)
        self.v_central.addWidget(self.background)


class SearchBox(QWidget):
    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout(self)
        # Search a person
        self.search_icon = QLabel()
        self.search_icon.setScaledContents(True)
        self.search_icon.setFixedSize(30, 30)
        self.search_icon.setPixmap(QPixmap(Icon.search))
        # Search entry
        self.search_entry = QLineEdit()
        self.search_entry.setFont(QFont('Ubuntu', 10))
        self.search_entry.setPlaceholderText('Search in your box')
        # Add to layout
        self.h_layout.addWidget(self.search_icon)
        self.h_layout.addWidget(self.search_entry)
        self.set_default()
        self.set_width(300)

    def set_width(self, width):
        self.setFixedWidth(width)

    def set_default(self):
        self.search_entry.setText("")


class InfoBox(QWidget):
    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(10, 5, 10, 5)
        self.h_layout.setSpacing(10)
        self.avatar = QLabel()
        self.avatar.setFixedSize(50, 50)
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners(Icon.elephant))
        # info
        self.name = QLabel('Dong Quoc Tranh')
        self.name.setStyleSheet('color:white')
        self.status_icon = QLabel()
        self.status_icon.setFixedSize(20, 20)
        self.status_icon.setStyleSheet(
            f'border-radius: {int(self.status_icon.width()/2)};  background: green;')
        self.status = QLabel()
        self.status.setStyleSheet('color:white')
        # Add name and status layout into horizontal layout
        self.h_name_icon = QHBoxLayout()
        self.h_name_icon.setAlignment(Qt.AlignLeft)
        self.h_name_icon.setSpacing(5)
        self.h_name_icon.addWidget(self.name)
        self.h_name_icon.addWidget(self.status_icon)
        # Add name_icon layout and status into vertical layout
        self.v_status = QVBoxLayout()
        self.v_status.setSpacing(10)
        self.v_status.addLayout(self.h_name_icon)
        self.v_status.addWidget(self.status)
        # Add to layout
        self.h_layout.addWidget(self.avatar)
        self.h_layout.addLayout(self.v_status)
        # Set default
        self.set_status(Status.offline)

    def _set_avatar(self, pixmap):
        rounded = round_corners(pixmap)
        self.avatar.setPixmap(rounded)

    def set_status(self, status):
        self.status.setText(status.name)
        # self.status_icon.setStyleSheet(status.style)

    def _set_name(self, name):
        self.name.setText(name)

    def update(self, name, avatar, status):
        self._set_name(name)
        self._set_avatar(avatar)
        self.set_status(status)

    ################################ Body ########################
    
class Body(BaseWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background: lightgreen')
        # Background
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(10)
        # dummy
        dummy = QLabel('asdasdasd')
        self.h_bg.addWidget(dummy)
        # Add to layout
        self.v_central.addWidget(self.background)


class ContactHistory(BaseWidget):
    def __init__(self, background_style, width):
        super().__init__()
        self.setStyleSheet(background_style)
        self.setFixedWidth(width)
        self.v_bg = QVBoxLayout(self.background)
        # Scroll Area
        self.history = QScrollArea()
        # Add to layout
        self.v_bg.addWidget(self.history)
    
    def add(self, contact):
        pass

    def remove(self, contact):
        pass


class Contact(BaseWidget):
    def __init__(self):
        super().__init__()
        # size policy
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.v_bg = QVBoxLayout(self.background)
        # Status
        self.online_time = QLabel("Right Now")
        self.staonline_timetus.setFont(QFont('Ubuntu', 8))
        self.online_time.setStyleSheet('color:white')
        self.online_time.setAlignment(Qt.AlignRight)
        # Contact info
        self.avatar = QLabel(round_corners(Icon.user))
        self.avatar.setFixedSize(50, 50)
        self.avatar.setScaledContents(True)

        # Add to layout:
        self.v_bg.addWidget(self.online_time)
        self.v_bg.addWidget(self.avatars)
    
    def mousePressEvent(self, event):
        print('Pressed in Contact')


class Conversation(BaseWidget):
    def __init__(self):
        super().__init__()
        self.v_bg = QVBoxLayout(self.background)
        # 


class ChatPiece(QWidget):
    def __init__(self):
        super().__init__()
        pass
