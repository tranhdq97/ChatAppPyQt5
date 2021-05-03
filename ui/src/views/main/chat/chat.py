import os
from datetime import date, datetime
from typing import Container
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QTextEdit
from PyQt5.QtWidgets import QScrollArea, QSizePolicy, QVBoxLayout, QWidget
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
    """ Containes searching place and Talker's information.
    """
    def __init__(self):
        super().__init__()
        # Size policy
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet('background:rgb(60, 90, 100)')
        # Background
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(0)
        self.search_box = SearchBox()
        self.info_box = TalkerInfo()
        # Add to layout
        self.h_bg.addWidget(self.search_box)
        self.h_bg.addWidget(self.info_box)
        self.v_central.addWidget(self.background)


class SearchBox(QWidget):
    """ Conversation or friend is searched by using name of person.
    """
    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout(self)
        self.on_contacts = False
        # Search a person
        self.search_icon = QLabel()
        self.search_icon.setScaledContents(True)
        self.search_icon.setFixedSize(27, 27)
        self.search_icon.setPixmap(QPixmap(Icon.search))
        # Search entry
        self.search_entry = QLineEdit()
        self.search_entry.setContentsMargins(5, 8, 5, 8)
        self.search_entry.setStyleSheet('color:rgb(230, 230, 230)')
        self.search_entry.setFont(QFont('Ubuntu', 12))
        self.search_entry.setPlaceholderText('Search in your box')
        # Contacts
        self.contacts = QPushButton()
        self.contacts.setFixedSize(35, 35)
        self.contacts.setFlat(True)
        set_icon(self.contacts, Icon.contacts)
        # Add to layout
        self.h_layout.addWidget(self.search_icon)
        self.h_layout.addWidget(self.search_entry)
        self.h_layout.addWidget(self.contacts)
        self.set_default()
        self.set_width(300)

    def set_width(self, width):
        self.setFixedWidth(width)

    def set_default(self):
        self.search_entry.setText("")

    def switch_contacts(self):
        if self.on_contacts: # to chats
            self.contacts.setStyleSheet(
                'QPushButton {background:transparent;border-radius: 3px}')
        else:
            self.contacts.setStyleSheet(
                'QPushButton {background:rgb(100,100,200);border-radius: 3px}')
        self.on_contacts = not self.on_contacts


class TalkerInfo(QWidget):
    """ Contains some basic info of partner that user talks to.
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
    """ Contains conversations' info, contacts and messages of current conversation. 
    """
    def __init__(self):
        super().__init__()
        # Background
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(10)
        # history
        self.history = Chats()
        self.conversation = Conversation()
        # Add to layout
        self.h_bg.addWidget(self.history)
        self.h_bg.addWidget(self.conversation)
        self.v_central.addWidget(self.background)

    def resizeEvent(self, a0):
        if self.width() < 700:
            self.history.setVisible(False)
        else:
            self.history.setVisible(True)
        return super().resizeEvent(a0)

    ##################################### Chats

class Chats(BaseWidget):
    """ Contains history of conversations which each conversation includes
        talker's name, avatar, last message,...
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background:rgb(0, 75, 100)')
        self.setFixedWidth(300)
        self.v_bg = QVBoxLayout(self.background)
        self._participants = []
        self._on_chats = True
        # self.contra
        # Scroll Area
        self.history = PersonContainer()
        self.contacts = PersonContainer()
        # Add to layout
        self.v_bg.addWidget(self.history)
        self.v_bg.addWidget(self.contacts)

        for i in range (10):
            self.add_convo(Talker())

        for i in range (1):
            self.add_friend(Talker())

        # Init
        self.set_default()
    
    def add_convo(self, talker):
        """ Adds new coversation.

        Args:
            talker (Talker): New partner.
        """
        self.history.v_content.addWidget(talker)
        self._participants.append(talker)
        
    def remove_convo(self, talker):
        """ Removes talker out of history list.

        Args:
            talker (Talker]): Ui of person who used to chat.
        """
        pass

    def add_friend(self, friend):
        """ Adds new friend to contact list.

        Args:
            friend: new friend.
        """
        self.contacts.v_content.addWidget(friend)

    def remove_friend(self, friend):
        """ Removes specific friend of of contact list.

        Args:
            friend (Friend): friend object
        """
        pass

    def set_default(self):
        self.history.setVisible(True)
        self.contacts.setVisible(False)

    def switch(self, on_contacts):
        """ Switchs between contacts and chats.
        """
        if on_contacts: # chats
            self.history.setVisible(True)
            self.contacts.setVisible(False)
        else:
            self.history.setVisible(False)
            self.contacts.setVisible(True)


class PersonContainer(QScrollArea):
    """ This container contains view of individuals (friends or talkers).
    """
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.NoFrame)
        self.setContentsMargins(-1, 0, -1, 0)
        self.setWidgetResizable(True)
        self.setStyleSheet(Style.scroll_area)
        # Widget content
        self.content = QWidget()
        self.v_content = QVBoxLayout(self.content)
        self.v_content.setContentsMargins(0, 0, 0, 0)
        self.v_content.setSpacing(10)
        self.v_content.setAlignment(Qt.AlignTop)
        self.setWidget(self.content)


class Talker(BaseWidget):
    """ A conversation.
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
        # talker info
        # self.avatar = AvatarWithStatus()
        self.avatar = QLabel()
        self.avatar.setFixedSize(50, 50)
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners(Icon.cat))
        # User name
        self.username = QLabel('Dong Quoc Tranh')
        self.username.setStyleSheet('color:white')
        self.username.setAlignment(Qt.AlignLeft)
        self.username.setFont(name_font)
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
        self.v_layout.addWidget(self.username)
        self.v_layout.addSpacing(5)
        self.v_layout.addLayout(self.h_activity)
        # Add to layout:
        self.h_bg.addWidget(self.avatar)
        self.h_bg.addLayout(self.v_layout)
    
    def mousePressEvent(self, event):
        print('Pressed in ', self.username.text())

    @property
    def name(self):
        return self.username.text()

    def set_default(self):
        self._conversation = Conversation()

    def send(self, text):
        pass

    def receive(self, text):
        pass


class Friend(BaseWidget):
    """ Ui of a friend.
    """
    def __init__(self):
        super().__init__()
        pass

    ##################################### Conversation

class Conversation(BaseWidget):
    """ Contains messages of a conversation.
    """
    def __init__(self):
        super().__init__()
        self._last_sender = None
        self.v_bg = QVBoxLayout(self.background)
        self.setMinimumWidth(300)
        # Scroller
        self.convo = PersonContainer()
        self.msg_entry = MessageEnter()
        self.msg_entry.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # Add to layout
        self.v_bg.addWidget(self.convo)
        self.v_bg.addWidget(self.msg_entry)

    def send(self, content):
        if self._last_sender is not None and self._last_sender.name == User.name:
            self._last_sender.send(content)
        else:           
            user = User()
            user.send(content)
            self.convo.v_content.addWidget(user)
            self._last_sender = user

        
    def receive(self, content):
        if self._last_sender is not None and self._last_sender.name == Partner.name:
            self._last_sender.send(content)
        else:
            partner = Partner()
            partner.send(content)
            self.convo.v_content.addWidget(partner)
            self._last_sender = partner


class ChatPiece(BaseWidget):
    """ Groups messages of a person.
    """
    def __init__(self, message_style):
        super().__init__()
        self._message_style = message_style
        self.background.setStyleSheet('background:transparent')
        self.background.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        time_font = QFont('Ubuntu', 10)
        self.fm = QFontMetrics(time_font)
        self._messages = []
        # background layout
        self.h_background = QHBoxLayout(self.background)
        # Massage layout
        self.v_messages = QVBoxLayout()
        self.v_messages.setSpacing(1)
        # Time
        self._date = datetime.today()
        self._time = datetime.now()
        self.time = QLabel(f'{self._time.strftime("%H:%M:%S")}')
        self.time.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.time.setFont(time_font)
        self.time.setStyleSheet('color:rgb(150,150,150)')
        # Add to layout
        self.v_time_msg = QVBoxLayout()
        self.v_time_msg.addWidget(self.time)
        self.v_time_msg.addLayout(self.v_messages)
        self.h_background.addLayout(self.v_time_msg)

    def send(self, content, is_user):
        """ Sends a message.

        Args:
            content (str): message content.
        """
        content_lbl = QLabel(content)
        content_lbl.setContentsMargins(10, 13, 10, 13)
        self._resize_label(content_lbl, int(0.6 * self.width()))
        content_lbl.setStyleSheet(self._message_style)
        content_lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        msg_layout = QHBoxLayout()
        if is_user:
            msg_layout.addWidget(content_lbl)
            msg_layout.setAlignment(Qt.AlignRight)

        else:
            msg_layout.addWidget(content_lbl)
            msg_layout.setAlignment(Qt.AlignLeft)

        self.v_messages.addLayout(msg_layout)
        self._date = datetime.today()
        self._time = datetime.now()
        self.time.setText(f'{self._time.strftime("%H:%M:%S")}')
        self._messages.append(content_lbl)

    def resizeEvent(self, a0):
        max_width = int(0.6*self.width())
        for msg in self._messages:
            self._resize_label(msg, max_width)
        return super().resizeEvent(a0)

    def _resize_label(self, label, max_width):
        content_width = label.fontMetrics().boundingRect(label.text()).width() + 30
        if content_width < max_width:
            label.setFixedWidth(content_width)
            label.setWordWrap(False)
        else:
            label.setFixedWidth(max_width)
            label.setWordWrap(True)


class User(ChatPiece):
    """ Chat peice of user
    """
    name = 'User'
    def __init__(self):
        message_style = """ 
            background: rgba(50,100,200,0.4);
            color:white;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        """
        super().__init__(message_style)
        self.time.setAlignment(Qt.AlignRight)
        self.v_messages.setAlignment(Qt.AlignRight)
        self.h_background.setAlignment(Qt.AlignRight)

    def send(self, content):
        super().send(content, is_user=True)


class Partner(ChatPiece):
    """Chat peice of partner.
    """
    name = 'Partner'
    def __init__(self):
        message_style = """ 
            background: rgba(50,50,50,0.4);
            color:white;
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        """
        super().__init__(message_style)
        self.time.setAlignment(Qt.AlignLeft)
        self.h_background.setAlignment(Qt.AlignLeft)
        self.v_messages.setAlignment(Qt.AlignLeft)
        self.avatar = QLabel()
        self.avatar.setFixedSize(50, 50)
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners(Icon.elephant))
        self.v_avatar = QVBoxLayout()
        self.v_avatar.setAlignment(Qt.AlignTop)
        self.v_avatar.addWidget(self.avatar)
        self.h_background.insertLayout(0, self.v_avatar)
        
    def send(self, content):
        super().send(content, is_user=False)


class MessageEnter(BaseWidget):
    """ Place for entering and sending message.
    """
    def __init__(self):
        super().__init__()
        self.h_background = QHBoxLayout(self.background)
        # Content entry
        self.content_edit = QTextEdit()
        self.content_edit.setFixedHeight(50)
        self.content_edit.setPlaceholderText('Please enter message ...')
        self.send_btn = QPushButton('>')
        self.send_btn.setFixedSize(50, 50)
        self.send_btn.setFlat(True)
        self.send_btn.setStyleSheet(
            f'background:rgb(200,200,255);color:white;border-radius:{int(self.send_btn.width()/2)}px')
        self.h_background.addWidget(self.content_edit)
        self.h_background.addWidget(self.send_btn)

    @property
    def content(self):
        return self.content_edit.toPlainText()


class AvatarWithStatus(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)
        # Avatar
        self.avatar = QLabel()
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners('ui/assets/icons/user.png'))
        self.avatar_widget = QWidget()
        self.avatar_widget.setStyleSheet('background:transparent')
        self.v_avatar = QVBoxLayout(self.avatar_widget)
        self.v_avatar.addWidget(self.avatar)
        self.v_avatar.setContentsMargins(0, 0, 0, 0)
        # Status icon
        self.status = QLabel()
        self.status.setFixedSize(20, 20)
        self.status.setStyleSheet(
            f'background:gray; border:2px solid white; border-radius:{int(self.status.height()/2)}px')
        self.status_widget = QWidget()
        self.status_widget.setStyleSheet('background:transparent')
        self.v_status = QVBoxLayout(self.status_widget)
        self.v_status.setContentsMargins(0, 0, 0, 0)
        self.v_status.addWidget(self.status)
        self.v_status.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        # Add to stackedwidget
        self.addWidget(self.status_widget)

        self.addWidget(self.avatar_widget)
        # self.addWidget(self.status_widget)
        # self.setCurrentIndex(0)
        self.setCurrentIndex(1)
        self.status_widget.setVisible(True)
        # print(self.avatar_widget.isVisible())
        # self.avatar_widget.setStyleSheet('background:blue')

        # self.avatar_widget.setEnabled(True)
        # self.avatar.setVisible(True)
        #         # print(self.status_widget.isVisible())
        # print(self.avatar_widget.isVisible())

        # print(self.count())