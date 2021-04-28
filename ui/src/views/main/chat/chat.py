from os import name
from PyQt5.QtGui import QFont, QTextBlockUserData
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QSizePolicy, QVBoxLayout, QWidget
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
    """[summary]

    Args:
        BaseWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        # Size policy
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet('background:rgb(0, 75, 100)')
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
    """[summary]

    Args:
        QWidget ([type]): [description]
    """
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
        self.search_entry.setContentsMargins(5, 8, 5, 8)
        self.search_entry.setStyleSheet('color:rgb(230, 230, 230)')
        self.search_entry.setFont(QFont('Ubuntu', 12))
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
    """[summary]

    Args:
        QWidget ([type]): [description]
    """
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
    """[summary]

    Args:
        BaseWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background: lightgreen')
        # Background
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(10)
        # Participant history
        self.Participant_history = Chats()

        # Add to layout
        self.v_central.addWidget(self.Participant_history)
        self.v_central.addWidget(self.background)


class Chats(BaseWidget):
    """[summary]

    Args:
        BaseWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background:rgb(0, 75, 100)')
        self.setFixedWidth(300)
        self.v_bg = QVBoxLayout(self.background)
        self._participants = []
        # Scroll Area
        self.history = QScrollArea()
        self.history.setFrameStyle(QFrame.NoFrame)
        self.history.setWidgetResizable(True)
        self.history.setStyleSheet(Style.scroll_area)
        self.history_contents = QWidget()
        self.v_h_c = QVBoxLayout(self.history_contents)
        self.v_h_c.setContentsMargins(0, 0, 0, 0)
        self.v_h_c.setSpacing(10)
        self.v_h_c.setAlignment(Qt.AlignTop)
        # Add to layout
        self.history.setWidget(self.history_contents)
        self.v_bg.addWidget(self.history)
        for i in range (10):
            self.add(Participant())
    
    def add(self, Participant):
        self.v_h_c.addWidget(Participant)
        self._participants.append(Participant)
        
    def remove(self, Participant):
        pass


class Participant(BaseWidget):
    """[summary]

    Args:
        BaseWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self._conversation = None
        # size policy
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.h_bg = QHBoxLayout(self.background)
        self.background.setStyleSheet(
            'background:rgb(0, 45, 60); border-radius: 20px')
        # Font
        online_time_font = QFont('Ubuntu', 8)
        name_font = QFont('Ubuntu', 14, QFont.Bold)
        last_msg_font = QFont('Ubuntu', 10)
        # Participant info
        self.avatar = QLabel()
        self.avatar.setPixmap(round_corners(Icon.cat))
        self.avatar.setFixedSize(50, 50)
        self.avatar.setScaledContents(True)
        # User name
        self.name = QLabel('Dong Quoc Tranh')
        self.name.setStyleSheet('color:white')
        self.name.setAlignment(Qt.AlignLeft)
        self.name.setFont(name_font)
        # The last massage
        self.last_msg = QLabel('Helllo adsssss .....')
        self.last_msg.setStyleSheet('color:rgb(200, 200, 200)')
        self.last_msg.setContentsMargins(5, 0, 0, 0)
        self.last_msg.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.last_msg.setFont(last_msg_font)
        # Activity time
        self.online_time = QLabel("Right Now")
        self.online_time.setWordWrap(True)
        self.online_time.setStyleSheet('color:white')
        self.online_time.setAlignment(Qt.AlignRight)
        self.online_time.setFont(online_time_font)
        self.h_activity = QHBoxLayout()
        self.h_activity.setContentsMargins(1, 1, 1, 1)
        self.h_activity.setSpacing(5)
        self.h_activity.addWidget(self.last_msg)
        self.h_activity.addWidget(self.online_time)
        # Person info
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.name)
        self.v_layout.addSpacing(5)
        self.v_layout.addLayout(self.h_activity)
        # Add to layout:
        self.h_bg.addWidget(self.avatar)
        self.h_bg.addLayout(self.v_layout)
    
    def mousePressEvent(self, event):
        print('Pressed in ', self.name.text())

    @property
    def name(self):
        return self.name.text()

    def set_default(self):
        self._conversation = Conversation()

    def send(self, text):
        pass

    def receive(self, text):
        pass



class Conversation(BaseWidget):
    """[summary]

    Args:
        BaseWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.v_bg = QVBoxLayout(self.background)
        # 


class ChatPiece(BaseWidget):
    """[summary]

    Args:
        QWidget ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        pass
