import sys
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QWidget


class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        self.setStyleSheet("background:rgb(3, 18, 30)")
        self.pressing = False
        self._is_maximized = False
        #
        self.background = QWidget()
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(2, 3, 2, 3)
        self.h_bg.setSpacing(2)
        # Title
        self.title = QLabel('OK')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont('Ubuntu', 12, QFont.Bold))
        # close button
        btn_size = 25
        self.btn_close = QPushButton("x")
        self.btn_close.setFixedSize(btn_size, btn_size)
        self.btn_close.setStyleSheet(
            f'background:red; color:white; border-radius:{int(btn_size/2)};')
        # minimize button 
        self.btn_min = QPushButton('-')
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet(
            f'background:gray; color:white; border-radius:{int(btn_size/2)};')
        # maximize button
        self.btn_max = QPushButton("+")
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet(
            f'background:green; color:white; border-radius:{int(btn_size/2)};')
        # Add to layout
        self.h_bg.addWidget(self.title)
        self.h_bg.addWidget(self.btn_min)
        self.h_bg.addWidget(self.btn_max)
        self.h_bg.addWidget(self.btn_close)
        self.v_central.addWidget(self.background)

    def set_background(self, style):
        self.setStyleSheet(style)

    def set_title(self, title):
        self.title.setText(title)

    # def resizeEvent(self, QResizeEvent):
        # pass

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(
                self.mapToGlobal(self.movement).x(),
                self.mapToGlobal(self.movement).y(),
                self.parent.width(), self.parent.height()
            )
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def close_app(self):
        self.parent.close()

    def minimize(self):
        self.parent.showMinimized()

    def maximize(self):
        print(self._is_maximized)
        if not self._is_maximized:
            self.parent.showMaximized()
        else:
            self.parent.resize(self.parent.geometry().size() * 0.7)
        self._is_maximized = not self._is_maximized