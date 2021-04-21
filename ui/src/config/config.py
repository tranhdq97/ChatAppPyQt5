from enum import Enum
from enum import unique
from collections import namedtuple


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


@unique
class Status(Enum):
    online          = ["Active Now", "QLabel {background:rgb(0, 196, 0)}"]
    busy            = ["Busy", "QLabel {background:rgb(230, 30, 16)}"]
    away            = ["Away", "QLabel {background:rgb(237, 142, 0)}"]
    offline         = ["Offline", "QLabel {background:rgb(207, 207, 207)}"]


class Style(object):
    border = 'border:2px solid red'

    class Tab(CustomEnum):
        chosen_bg           = 'background:rgb(81, 121, 194)'


class Tab(CustomEnum):
    chat                    = 'Chat'
    home                    = 'Home'
