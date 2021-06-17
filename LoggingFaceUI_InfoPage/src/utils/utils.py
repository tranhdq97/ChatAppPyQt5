from PyQt5.QtGui import QPixmap, QPen, QPainter, QBrush, QPainterPath
from PyQt5.QtCore import Qt, QSize, QRect, QMargins


def round_corners(pixmap, radius=None, border=20):
    """ Rounds corners of an image.
    Args:
        path (str): path of image
    """
    if radius is None:
        radius = min(pixmap.height(), pixmap.width())

    rounded_pixmap = QPixmap(pixmap.size())
    rounded_pixmap.fill(Qt.transparent)
    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QBrush(pixmap))
    painter.setPen(QPen(Qt.white, border, Qt.SolidLine))
    painter.drawRoundedRect(pixmap.rect() - QMargins(border, border, 2 * border, 2 * border),
                            radius, radius)

    return rounded_pixmap
