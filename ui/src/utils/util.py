import PyQt5
from PyQt5.QtGui import QBrush, QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize
from ..configs.config import Icon


def round_corners(path=Icon.cat, radius=None, pixmap=None):
    """ Rounds corners of an image.

    Args:
        path (str): path of image
    """
    if pixmap is None:
        pixmap = QPixmap(path)
    if radius is None:
        radius = min(pixmap.height(), pixmap.width())

    rounded_pixmap = QPixmap(pixmap.size())
    rounded_pixmap.fill(Qt.transparent)
    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QBrush(pixmap))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(pixmap.rect(), radius, radius)

    return rounded_pixmap


def set_icon(btn, image, margin=5):
    """ Sets icon to button. 

    Args:
        btn (QPushButton): button
        image (str): the path of icon / QPixmap
    """
    if isinstance(image, str):
        image = QPixmap(image)
    icon = QIcon()
    icon.addPixmap(image)
    btn.setIcon(icon)
    btn.setIconSize(QSize(btn.width() - margin, btn.height() - margin))
