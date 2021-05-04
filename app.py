import sys
from PyQt5 import QtWidgets
from ui.src.controllers.controller import MainController
from TestPage import Main
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QtWidgets.QApplication(sys.argv)
# window = MainController()
window = Main()
window.show()
sys.exit(app.exec_())