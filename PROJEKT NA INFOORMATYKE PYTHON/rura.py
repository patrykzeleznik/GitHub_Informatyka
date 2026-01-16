from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtCore import Qt, QTimer, QPointF

class Rura:
    def __init__(self, punkty, grubosc = 15, kolor=Qt.white):
        self.punkty = [QPointF(float (p[0]), float(p[1])) for p in punkty]
        self.grubosc = grubosc
        self.kolor_rury = kolor
        self.kolor_cieczy = QColor(0, 180, 255)
        self.czy_plynie = False
        
    def ustawienie_przeplywu(self, plynie):
        self.czy_plynie = plynie
        
    def rysowanie(self, painter):
        if len(self.punkty) < 2:
            return
        path = QPainterPath()
        path.moveTo(self.punkty[0])
        for p in self.punkty[1:]:
            path.lineTo(p)
        olowek_rury = QPen(self.kolor_rury, self.grubosc, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(olowek_rury)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)
        if self.czy_plynie:
            pen_ciecz = QPen(self.kolor_cieczy, self.grubosc - 4, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen_ciecz)
            painter.drawPath(path)
        
        

