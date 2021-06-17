from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStackedWidget, QScrollArea, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from ..utils.utils import round_corners


class InfoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.scroll = QScrollArea()
        self.scroll.setContentsMargins(0, 0, 0, 0)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        # self.scroll_content.setStyleSheet('background: rgb(200, 240, 220); border:2px solid black;')
        self.scroll.setWidget(self.scroll_content)
        self.v_scroll_content = QVBoxLayout(self.scroll_content)
        self.v_scroll_content.setContentsMargins(0, 0, 0, 0)
        self.v_scroll_content.setSpacing(0)
        
        # General info
        self.general_info = GeneralInfo()


        # Add to scroll area
        self.v_scroll_content.addWidget(self.general_info)


        # Add to layout
        
        self.v_central.addWidget(self.scroll)

class CustomWidget(QStackedWidget):
    """This widget contains 2 layers, named background and foreground.
    It helps to show both layers.
    """
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        # Background
        self.background = QWidget()
        self.background.setMinimumSize(100, 100)
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.bg_img = QLabel()
        self.bg_img.setFixedHeight(100)
        self.bg_img.setScaledContents(True)
        # Foreground
        self.foreground = QWidget()
        self.foreground.setStyleSheet("background:transparent")
        # Add to layout
        self.v_bg.addWidget(self.bg_img)
        self.addWidget(self.background)
        self.addWidget(self.foreground)
        self.set_default()
    
    def set_default(self):
        self.setCurrentIndex(1)
        self.background.setVisible(True)
    
    def set_bg_img(self, pixmap):
        self.bg_img.setPixmap(pixmap)

    def resizeEvent(self, e):
        self.background.resize(self.width(), self.height())


class GeneralInfo(CustomWidget):
    def __init__(self):
        super().__init__()

        # Background
        self.set_bg_img(QPixmap('src/asserts/leaves.png'))
        self.bg_bottomhalf = QLabel()
        self.v_bg.addWidget(self.bg_bottomhalf)

        # Foreground
        self.v_fg = QVBoxLayout(self.foreground)
        self.v_fg.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # Avatar
        self.avatar = QLabel()
        self.avatar.setFixedSize(150, 150)
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(round_corners(QPixmap('src/asserts/person.png')))
        self.h_avatar = QHBoxLayout()
        self.h_avatar.setContentsMargins(0, 30, 0, 0)
        # Info
        self.name = QLabel('Dong Quoc Tranh')
        self.name.setFont(QFont('Arial', 17, QFont.Bold))
        self.name.setAlignment(Qt.AlignHCenter)
        self.grip_info = QGridLayout()
        self.grip_info.setAlignment(Qt.AlignLeft)
        # General info
        self.username = BasicForm('username', value='tranhdq')
        self.email = BasicForm('email', value='tranhdq@gmail.com')

        

        # Add to layout
        self.h_avatar.addWidget(self.avatar)
        self.grip_info.addLayout(self.username, 0, 0)
        self.grip_info.addLayout(self.email, 0, 1)
        self.v_fg.addLayout(self.h_avatar)
        self.v_fg.addWidget(self.name)
        self.v_fg.addLayout(self.grip_info)

    
class BasicForm(QHBoxLayout):
    def __init__(self, label, value="", label_width=100, label_height=20):   
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.label_font = QFont('Ubuntu', 10, QFont.Bold)
        self.value_font = QFont('Ubuntu', 10)
        self.label = QLabel(label)
        self.label.setStyleSheet("background: gray; border-top-right-radius: 10px; border-bottom-right-radius: 10px; color:white;")
        self.label.setFont(self.label_font)
        self.label.setFixedSize(label_width, label_height)
        self.label.setAlignment(Qt.AlignVCenter)
        self.label.setMargin(5)
        self.value = QLabel(value)
        self.value.setFont(self.value_font)
        self.value.setAlignment(Qt.AlignVCenter)
        self.value.setContentsMargins(10, 10, 10, 10)

        # Add to layout
        self.addWidget(self.label)
        self.addWidget(self.value)
