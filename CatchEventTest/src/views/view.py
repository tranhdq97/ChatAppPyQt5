from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel

from PyQt5.QtCore import QMetaObject, Qt
from .components import BaseWidget


class MainUI(object):
    def setupUi(self, MainWindow):
        self.main_widget = BaseWidget()
        self.main_widget.setStyleSheet('background:rgb(34,56,56)')
        self.v_background = QVBoxLayout(self.main_widget.background)
        self.v_background.setAlignment(Qt.AlignCenter)

        self.child = BaseWidget()
        self.child.setObjectName('Child1')
        self.child.setFixedSize(100, 200)
        self.child.background.setStyleSheet('border:2px solid green; background:green')
        self.v_child_bg = QVBoxLayout(self.child.background)
        self.label = QLabel()
        self.label.setFixedSize(100, 20)
        self.label.setStyleSheet('background:red')
        self.v_child_bg.addWidget(self.label)

        self.child2 = BaseWidget()
        self.child2.setObjectName('Child2')
        self.child2.setFixedSize(100, 200)
        self.child2.background.setStyleSheet('border:2px solid green; background:green')
        self.v_child2_bg = QVBoxLayout(self.child2.background)
        self.label = QLabel()
        self.label.setFixedSize(100, 20)
        self.label.setStyleSheet('background:red')
        self.v_child2_bg.addWidget(self.label)

        # add to layout 
        self.v_background.addWidget(self.child)
        self.v_background.addWidget(self.child2)


        MainWindow.setCentralWidget(self.main_widget)
        QMetaObject.connectSlotsByName(MainWindow)
