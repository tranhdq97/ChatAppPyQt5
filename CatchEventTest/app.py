import sys
import signal
from PyQt5.QtWidgets import QApplication
from src.controllers.controller import MainController


signal.signal(signal.SIGINT, signal.SIG_DFL)


app = QApplication(sys.argv)
window = MainController()
window.show()

sys.exit(app.exec_())