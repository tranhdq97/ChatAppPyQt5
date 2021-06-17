from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QEvent
from ..views import MainUI


class MainController(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.ui.child.installEventFilter(self)
        self.ui.child2.installEventFilter(self)

        """You could store all object that you need to catch touch event in a list,
        then installEventFilter through loop and override eventFilter method at controller"""

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.change_style(obj)

        if event.type() == QEvent.Leave:
            self.set_default(obj)

        if event.type() == QEvent.MouseButtonPress:
            self.mouse_clicked(obj)
        
        return super().eventFilter(obj, event)


    def change_style(self, obj):
        obj.background.setStyleSheet('background:rgb(200, 200, 200)')

    def set_default(self, obj):
        obj.background.setStyleSheet('background:black')

    def mouse_clicked(self, obj):
        obj.background.setStyleSheet('background:green')
