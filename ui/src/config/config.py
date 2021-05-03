from enum import Enum
from enum import unique
from collections import namedtuple
from os import stat

from PyQt5.QtWidgets import QScrollArea


class CustomEnum(Enum):
    def __get__(self, *args):
        return self.value


class Icon(CustomEnum):
    cat             = 'ui/assets/icons/cat.png'
    elephant        = 'ui/assets/icons/elephant.png'
    chat            = 'ui/assets/icons/messenger.png'
    home            = 'ui/assets/icons/elephant.png'
    maximize        = 'ui/assets/icons/maximize.png'
    restore         = 'ui/assets/icons/restore.png'
    search          = 'ui/assets/icons/search.png'
    user            = 'ui/assets/icons/user.png'
    contacts        = 'ui/assets/icons/contacts.png'


status = namedtuple('Status', ['name', 'style'])
@unique
class Status(CustomEnum):
    online          = status("Active Now", "QLabel {background:rgb(0, 196, 0)}")
    busy            = status("Busy", "QLabel {background:rgb(230, 30, 16)}")
    away            = status("Away", "QLabel {background:rgb(237, 142, 0)}")
    offline         = status("Offline", "QLabel {background:rgb(207, 207, 207)}")


class Style(object):
    border = 'border:2px solid red'
    scroll_area = """
        QScrollArea {border:none;}
        QScrollBar {background:transparent;}
        QScrollBar:vertical {width: 6px;}
        QScrollBar:horizontal {height: 6px;}
        QScrollBar::handle {background:green; border-radius: 3px;}
        QScrollBar::handle:vertical {width: 10px; min-height: 10px;}
        QScrollBar::add-line {border: none; background: none;}
        QScrollBar::sub-line {border: none; background: none;}   
    """

    class Tab(CustomEnum):
        chosen_bg           = 'background:rgb(0, 75, 100)'


class Tab(CustomEnum):
    chat                    = 'Chat'
    home                    = 'Home'


