https://github.com/Tsatthienmach/ChatAppPyQt5.gitfrom PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QLabel
from PyQt5.QtGui import QPixmap


class TwoLayerWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QLabel()
        self.background_frame.setScaledContents(True)
        self.background = QWidget()
        self.v_bg = QVBoxLayout(self.background)
        self.v_bg.addWidget(self.background_frame)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.background.setMinimumSize(100, 100)
        self.addWidget(self.background)

    def set_foreground(self, widget):
        widget.setStyleSheet('background: transparent')
        if self.count() >= 2:
            self.removeWidget(self.currentWidget())
        index = self.addWidget(widget)
        self.setCurrentIndex(index)
        self.background.setVisible(True)

    def set_background(self, image):
        self.background_frame.setPixmap(QPixmap(image))

    def resizeEvent(self, e):
        self.background.resize(self.width(), self.height()) 

