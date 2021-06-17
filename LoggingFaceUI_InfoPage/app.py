from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import signal
from src.controllers.controller import MainController

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__=='__main__':

    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec_())
