import sys

from random import randrange as r
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        red, g, b = r(0, 256), r(0, 256), r(0, 256)
        qp.setBrush(QColor(red, g, b))
        qp.setPen(QColor(red, g, b))
        n = r(5, 400)
        qp.drawEllipse(80, 110, n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
