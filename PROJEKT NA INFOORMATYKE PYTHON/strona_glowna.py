import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath, QFont
from PyQt5.QtCore import Qt, QTimer, QPointF
from elementy_graficzne import moje_elementy_graficzne
from logika_gry import ustaw_logike

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projekt - Przelewanie sie wody pomiedzy zbiornikami")
        self.setFixedSize(900,650)
        self.setStyleSheet("background-color: #222;")
        
        moje_elementy_graficzne(self)
        
        ustaw_logike(self)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        font_header = QFont("Impact", 16)
        painter.setFont(font_header)
        painter.setPen(Qt.white) 
        painter.drawText(300, 20, self.width(), 80, Qt.AlignCenter, "Regulator Poziomu\ni\nTemperatury w Zbiornikach")
        painter.setFont(QFont("Segoe UI", 9))
        for i in range(1, 12): getattr(self, f'r{i}').rysowanie(painter)
        for i in range(1, 6): getattr(self, f'z{i}').draw(painter)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()   
    sys.exit(app.exec_())


