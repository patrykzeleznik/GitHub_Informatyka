import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtCore import Qt, QTimer, QPointF
from rura import Rura

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projekt - Przelewanie sie wody pomiedzy zbiornikami")
        self.setFixedSize(900,650)
        self.setStyleSheet("background-color: #232;")
        
        self.rura_testowa = Rura([(100,110),(100, 100), (300, 100), (300,90)], grubosc=20)
        self.rura_testowa.czy_plynie = True
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.rura_testowa.rysowanie(painter)      
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()   
    sys.exit(app.exec_())

