import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtCore import Qt, QTimer, QPointF
from rura import Rura
from zbiornik import Zbiornik

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projekt - Przelewanie sie wody pomiedzy zbiornikami")
        self.setFixedSize(900,650)
        self.setStyleSheet("background-color: #222;")
        
        self.r1 = Rura([(184,340),(184, 280), (324, 280), (324,220)], grubosc=15)
        self.r2 = Rura([(704,340),(704, 280), (564, 280), (564,220)], grubosc=15)
        self.r3 = Rura([(304, 500), (304, 450), (144,450), (144,400)], grubosc=15)
        self.r4 = Rura([(584, 500), (584, 450), (744,450), (744, 400)], grubosc=15)
        self.r5 = Rura([(450,0),(450,60)], grubosc=10)
        self.r6 = Rura([(0,370),(134,370)], grubosc=10)
        self.r7 = Rura([(0,530),(254,530)], grubosc=10)
        self.r8 = Rura([(900,370),(744,370)], grubosc=10)
        self.r9 = Rura([(900,530),(634,530)], grubosc=10)
        self.r10 = Rura([(354,530),(374,530),(374,650)], grubosc=10)
        self.r11 = Rura([(534,530),(514,530),(514,650)], grubosc=10)
        
        self.z1 = Zbiornik(294,50,300,180, "ZBIORNIK 1")
        self.z2 = Zbiornik(124,330, 120, 80, "ZBIORNIK 2")
        self.z3 = Zbiornik(644,330, 120, 80, "ZBIORNIK 3")
        self.z4 = Zbiornik(524,490, 120, 80, "ZBIORNIK 5")
        self.z5 = Zbiornik(244,490, 120, 80, "ZBIORNIK 4")
        
        self.flow_speed = 0.8
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda: self.pompowanie_cieczy(1))
        self.btn1 = QPushButton("Pompuj", self)
        self.btn1.setGeometry(475, 10, 80, 30)
        self.btn1.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn1.clicked.connect(lambda: self.przelacz_symulacje(1))
        self.running1 = False
        
        self.timer2 = QTimer()
        self.timer2.timeout.connect(lambda: self.pompowanie_cieczy(2))
        self.btn2 = QPushButton("Pompuj", self)
        self.btn2.setGeometry(10, 325, 80, 30)
        self.btn2.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn2.clicked.connect(lambda: self.przelacz_symulacje(2))
        self.running2 = False
        
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.logika_przeplywu)
        self.btn3 = QPushButton("Otworz zawory", self)
        self.btn3.setGeometry(10, 10, 120, 30)
        self.btn3.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn3.clicked.connect(lambda: self.przelacz_symulacje(3))
        self.running3 = False
        
        self.timer4 = QTimer()
        self.timer4.timeout.connect(lambda: self.pompowanie_cieczy(3))
        self.btn4 = QPushButton("Pompuj", self)
        self.btn4.setGeometry(790, 325, 80, 30)
        self.btn4.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn4.clicked.connect(lambda: self.przelacz_symulacje(4))
        self.running4 = False
        
        self.timer5 = QTimer()
        self.timer5.timeout.connect(lambda: self.pompowanie_cieczy(4))
        self.btn5 = QPushButton("Pompuj", self)
        self.btn5.setGeometry(790, 485, 80, 30)
        self.btn5.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn5.clicked.connect(lambda: self.przelacz_symulacje(5))
        self.running5 = False
        
        self.timer6 = QTimer()
        self.timer6.timeout.connect(lambda: self.pompowanie_cieczy(5))
        self.btn6 = QPushButton("Pompuj", self)
        self.btn6.setGeometry(10, 485, 80, 30)
        self.btn6.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn6.clicked.connect(lambda: self.przelacz_symulacje(6))
        self.running6 = False
        
        self.timer7 = QTimer()
        self.timer7.timeout.connect(lambda: self.odpompowanie_cieczy(1))
        self.btn7 = QPushButton("Odpompuj", self)
        self.btn7.setGeometry(274, 610, 80, 30)
        self.btn7.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn7.clicked.connect(lambda: self.przelacz_symulacje(7))
        self.running7 = False
        
        self.timer8 = QTimer()
        self.timer8.timeout.connect(lambda: self.odpompowanie_cieczy(2))
        self.btn8 = QPushButton("Odpompuj", self)
        self.btn8.setGeometry(534, 610, 80, 30)
        self.btn8.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
        self.btn8.clicked.connect(lambda: self.przelacz_symulacje(8))
        self.running8 = False
        
    def przelacz_symulacje(self, nr_procesu):
        if nr_procesu == 1:
            if self.running1:
                self.timer1.stop()
                self.r5.ustawienie_przeplywu(False)
                self.btn1.setText("Wznow")
            else:
                self.timer1.start(20)
                self.btn1.setText("Zatrzymaj")
            self.running1 = not self.running1
            self.update()
            
        elif nr_procesu == 2:
            if self.running2:
                self.timer2.stop()
                self.r6.ustawienie_przeplywu(False)
                self.btn2.setText("Wznow")
            else:
                self.timer2.start(20)
                self.btn2.setText("Zatrzymaj")
            self.running2 = not self.running2
            self.update()
            
        elif nr_procesu == 3:
            if self.running3:
                self.timer3.stop()
                for r in [self.r1, self.r2, self.r3, self.r4]:
                    r.ustawienie_przeplywu(False)
                self.btn3.setText("Otworz")
            else:
                self.timer3.start(20)
                self.btn3.setText("Zamknij")
            self.running3 = not self.running3
            self.update()
            
        elif nr_procesu == 4:
            if self.running4:
                self.timer4.stop()
                self.r8.ustawienie_przeplywu(False)
                self.btn4.setText("Wznow")
            else:
                self.timer4.start(20)
                self.btn4.setText("Zatrzymaj")
            self.running4 = not self.running4
            self.update()
            
        elif nr_procesu == 5:
            if self.running5:
                self.timer5.stop()
                self.r9.ustawienie_przeplywu(False)
                self.btn5.setText("Wznow")
            else:
                self.timer5.start(20)
                self.btn5.setText("Zatrzymaj")
            self.running5 = not self.running5
            self.update()
            
        elif nr_procesu == 6:
            if self.running6:
                self.timer6.stop()
                self.r7.ustawienie_przeplywu(False)
                self.btn6.setText("Wznow")
            else:
                self.timer6.start(20)
                self.btn6.setText("Zatrzymaj")
            self.running6 = not self.running6
            self.update()
            
        elif nr_procesu == 7:
            if self.running7:
                self.timer7.stop()
                self.r10.ustawienie_przeplywu(False)
                self.btn7.setText("Wznow")
            else:
                self.timer7.start(20)
                self.btn7.setText("Zatrzymaj")
            self.running7 = not self.running7
            self.update()
            
        elif nr_procesu == 8:
            if self.running8:
                self.timer8.stop()
                self.r11.ustawienie_przeplywu(False)
                self.btn8.setText("Wznow")
            else:
                self.timer8.start(20)
                self.btn8.setText("Zatrzymaj")
            self.running8 = not self.running8
            self.update()
        
    def pompowanie_cieczy(self, nr_procesu):
        pompowanie = False
    
        if nr_procesu == 1:
            if not self.z1.czy_pelny():
                self.z1.dodaj_ciecz(0.5)
                pompowanie = True
                self.r5.ustawienie_przeplywu(pompowanie)
            else:
                self.r5.ustawienie_przeplywu(False)
        
        elif nr_procesu == 2:
            if not self.z2.czy_pelny():
                self.z2.dodaj_ciecz(0.5)
                pompowanie = True
                self.r6.ustawienie_przeplywu(pompowanie)
            else:
                self.r6.ustawienie_przeplywu(False)
        
        elif nr_procesu == 3:
            if not self.z3.czy_pelny():
                self.z3.dodaj_ciecz(0.5)
                pompowanie = True
                self.r8.ustawienie_przeplywu(pompowanie)
            else:
                self.r8.ustawienie_przeplywu(False)
        
        elif nr_procesu == 4:
            if not self.z4.czy_pelny():
                self.z4.dodaj_ciecz(0.5)
                pompowanie = True
                self.r9.ustawienie_przeplywu(pompowanie)
            else:
                self.r9.ustawienie_przeplywu(False)
        
        elif nr_procesu == 5:
            if not self.z5.czy_pelny():
                self.z5.dodaj_ciecz(0.5)
                pompowanie = True
                self.r7.ustawienie_przeplywu(pompowanie)
            else:
                self.r7.ustawienie_przeplywu(False)

        self.update()
        
    def odpompowanie_cieczy(self, nr_procesu):
        odpompowanie = False
        
        if nr_procesu == 1:
            if not self.z5.czy_pusty():
                self.z5.usun_ciecz(5)
                odpompowanie = True
                self.r10.ustawienie_przeplywu(odpompowanie)
            else:
                self.r10.ustawienie_przeplywu(False)
                
        elif nr_procesu == 2:
            if not self.z4.czy_pusty():
                self.z4.usun_ciecz(5)
                odpompowanie = True
                self.r11.ustawienie_przeplywu(odpompowanie)
            else:
                self.r11.ustawienie_przeplywu(False)
        
        self.update()
        
    def logika_przeplywu(self):
        out_speed = self.flow_speed / 2 
        plynie_1 = False
        plynie_2 = False
        if self.z1.aktualna_ilosc > 4:
            if not self.z2.czy_pelny():
                wsad = self.z1.usun_ciecz(out_speed)
                self.z2.dodaj_ciecz(wsad)
                plynie_1 = True
            if not self.z3.czy_pelny():
                wsad = self.z1.usun_ciecz(out_speed)
                self.z3.dodaj_ciecz(wsad)
                plynie_2 = True
            self.r1.ustawienie_przeplywu(plynie_1)
            self.r2.ustawienie_przeplywu(plynie_2)
                
        plynie_3 = False
        if self.z2.aktualna_ilosc > 0.1 and not self.z5.czy_pelny():
            wsad = self.z2.usun_ciecz(out_speed)
            self.z5.dodaj_ciecz(wsad)
            plynie_3 = True
            self.r3.ustawienie_przeplywu(plynie_3)
        plynie_4 = False
        if self.z3.aktualna_ilosc > 0.1 and not self.z4.czy_pelny():
            wsad = self.z3.usun_ciecz(out_speed)
            self.z4.dodaj_ciecz(wsad)
            plynie_4 = True
            self.r4.ustawienie_przeplywu(plynie_4)  
        self.update()        
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.r1.rysowanie(painter)
        self.r2.rysowanie(painter)
        self.r3.rysowanie(painter)
        self.r4.rysowanie(painter)
        self.r5.rysowanie(painter)
        self.r6.rysowanie(painter)
        self.r7.rysowanie(painter)
        self.r8.rysowanie(painter)
        self.r9.rysowanie(painter)
        self.r10.rysowanie(painter)
        self.r11.rysowanie(painter)
        self.z1.draw(painter)
        self.z2.draw(painter)
        self.z3.draw(painter)
        self.z4.draw(painter)
        self.z5.draw(painter)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()   
    sys.exit(app.exec_())

