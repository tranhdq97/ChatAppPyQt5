import sys
from PyQt5 import QtWidgets
from ui.src.controllers.controller import MainController
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QtWidgets.QApplication(sys.argv)
window = MainController()
window.show()
sys.exit(app.exec_())