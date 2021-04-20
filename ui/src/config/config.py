from enum import Enum
from enum import unique
from collections import namedtuple


class CustomEnum(Enum):
    def __get__(self, *args):
        return self.value


class Icon(CustomEnum):
    cat             = 'ui/assets/icons/cat.png'
    elephant        = 'ui/assets/icons/elephant.png'
    messenger       = 'ui/assets/icons/messenger.png'
    maximize        = 'ui/assets/icons/maximize.png'
    restore         = 'ui/assets/icons/restore.png'


class Style(CustomEnum):
    border = 'border:2px solid red'