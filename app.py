import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.src.controllers.controller import MainController


app = QApplication(sys.argv)
window = MainController()
sys.exit(app.exec_())