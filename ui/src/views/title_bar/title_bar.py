import sys
from PyQt5.QtCore import QPoint, Qt, QSize, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from ...utils.util import *
from ...config.config import *


class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        self.setStyleSheet("background:rgb(3, 18, 30); color: white")
        self.pressing = False
        self._restore_pos = None
        self._restore_size = None
        # Background
        self.background = QWidget()
        self.h_bg = QHBoxLayout(self.background)
        self.h_bg.setContentsMargins(2, 5, 2, 5)
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
        # Minimize button 
        self.btn_min = QPushButton('-')
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet(
            f'background:gray; color:white; border-radius:{int(btn_size/2)};')
        # Maximize button
        self.btn_max = QPushButton()
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet(
            f'background:green; color:white; border-radius:{int(btn_size/2)};')
        set_icon(self.btn_max, Icon.maximize, margin=10)
        # Restore button
        self.btn_restore = QPushButton()
        self.btn_restore.setFixedSize(btn_size, btn_size)
        self.btn_restore.setStyleSheet(
            f'background:green; color:white; border-radius:{int(btn_size/2)};')
        set_icon(self.btn_restore, Icon.restore, margin=10)
        # Add to layout
        self.h_bg.addWidget(self.title)
        self.h_bg.addWidget(self.btn_min)
        self.h_bg.addWidget(self.btn_restore)
        self.h_bg.addWidget(self.btn_max)
        self.h_bg.addWidget(self.btn_close)
        self.v_central.addWidget(self.background)
        # Init
        self.set_default()

    def set_default(self):
        self.btn_restore.hide()

    def set_background(self, style):
        self.setStyleSheet(style)

    def set_title(self, title):
        self.title.setText(title)

    def close_app(self):
        self.parent.close()

    def minimize(self):
        self.parent.showMinimized()

    def maximize(self):
        self.btn_max.setVisible(False)
        self.btn_restore.setVisible(True)
        self._save_restore_info(self.parent.pos(), QSize(self.parent.width(),
                                self.parent.height()))
        desktop_rect = QApplication.desktop().availableGeometry()
        fact_rect = QRect(desktop_rect.x() - 3, desktop_rect.y() - 3,
                          desktop_rect.width() + 6, desktop_rect.height() + 6)
        self.parent.setGeometry(fact_rect)
        self.parent.setFixedSize(desktop_rect.width() + 6, desktop_rect.height() + 6)

    def restore(self):
        self.btn_max.setVisible(True)
        self.btn_restore.setVisible(False)
        window_pos, window_size = self._get_restore_info()
        self.parent.setGeometry(window_pos.x(), window_pos.y(),
                                window_size.width(), window_size.height())
        self.parent.setFixedSize(window_size.width(), window_size.height())

    def _get_restore_info(self):
        return self._restore_pos, self._restore_size

    def _save_restore_info(self, point, size):
        self._restore_pos = point
        self._restore_size = size

    ############################ Signals ################################

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
