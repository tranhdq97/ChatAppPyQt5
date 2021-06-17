from PyQt5.QtWidgets import QWidget, QVBoxLayout


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.v_central = QVBoxLayout(self)
        self.v_central.setContentsMargins(0, 0, 0, 0)
        self.v_central.setSpacing(0)
        # Background
        self.background = QWidget()
        # Add to layout
        self.v_central.addWidget(self.background)
