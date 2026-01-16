from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtCore import Qt, QTimer, QPointF

class Zbiornik:
    def __init__(self, x, y, width, height, nazwa=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nazwa = nazwa
        self.pojemnosc = 100.0
        self.aktualna_ilosc = 0.0
        self.poziom = 0.0
        self.temp = 0.0
        
    def dodaj_ciecz(self, ilosc):
        wolne = self.pojemnosc - self.aktualna_ilosc
        dodano = min(ilosc, wolne)
        self.aktualna_ilosc += dodano
        self.aktualizuj_poziom()
        return dodano
    
    def usun_ciecz(self, ilosc):
        usunieto = min(ilosc, self.aktualna_ilosc)
        self.aktualna_ilosc -= usunieto
        self.aktualizuj_poziom()
        return usunieto
    
    def aktualizuj_poziom(self):
        self.poziom = self.aktualna_ilosc / self.pojemnosc

    def czy_pusty(self):
        return self.aktualna_ilosc <= 0.1

    def czy_pelny(self):
        return self.aktualna_ilosc >= self.pojemnosc - 0.1
    
    def pobierz_kolor(self):
        t = self.temp / 100.0   
        if t < 0.5:        
            factor = t * 2
            r = int(255 * factor)
            g = int(120 + (255 - 120) * factor)
            b = 255
        else:
            factor = (t - 0.5) * 2
            r = 255
            g = int(255 * (1 - factor))
            b = int(255 * (1 - factor))
        
        return QColor(r, g, b)
    
    def draw(self, painter):
        if self.poziom > 0:
            h_cieczy = self.poziom * self.height
            y_start = self.y + self.height - h_cieczy
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.pobierz_kolor())
            painter.drawRect(int(self.x + 3), int(y_start), int(self.width - 6), int(h_cieczy - 2))
        pen = QPen(Qt.black, 3)
        pen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(int(self.x), int(self.y), int(self.width), int(self.height))
        pen = QPen(Qt.white)
        painter.setPen(pen)
        painter.drawText(int(self.x + self.width/2 - 21), int(self.y + self.height + 20), self.nazwa)
        font = painter.font()
        font.setPointSize(6)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(Qt.black)
        tekst_poziom = f"Poziom: {self.aktualna_ilosc:.1f} [mm]"
        tekst_temp = f"Temp: {self.temp:.1f} [°C]"
        painter.drawText(self.x, self.y + self.height - 40, self.width, 20, Qt.AlignCenter, tekst_poziom)
        painter.drawText(self.x, self.y + self.height - 20, self.width, 20, Qt.AlignCenter, tekst_temp)
            
            