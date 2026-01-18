from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QTimer

def ustaw_logike(app):
    def przelacz_symulacje(nr_procesu):
        if nr_procesu == 1:
            if app.running1:
                app.timer1.stop()
                app.r5.ustawienie_przeplywu(False)
                app.btn1.setText("Wznow")
            else:
                app.timer1.start(20)
                app.btn1.setText("Zatrzymaj")
            app.running1 = not app.running1
            app.update()
        elif nr_procesu == 2:
            if app.running2:
                app.timer2.stop()
                app.r6.ustawienie_przeplywu(False)
                app.btn2.setText("Wznow")
            else:
                app.timer2.start(20)
                app.btn2.setText("Zatrzymaj")
            app.running2 = not app.running2
            app.update()
        elif nr_procesu == 3:
            if app.running3:
                app.timer3.stop()
                for r in [app.r1, app.r2, app.r3, app.r4]:
                    r.ustawienie_przeplywu(False)
                app.btn3.setText("Otworz")
            else:
                app.timer3.start(20)
                app.btn3.setText("Zamknij")
            app.running3 = not app.running3
            app.update()
        elif nr_procesu == 4:
            if app.running4:
                app.timer4.stop()
                app.r8.ustawienie_przeplywu(False)
                app.btn4.setText("Wznow")
            else:
                app.timer4.start(20)
                app.btn4.setText("Zatrzymaj")
            app.running4 = not app.running4
            app.update()
        elif nr_procesu == 5:
            if app.running5:
                app.timer5.stop()
                app.r9.ustawienie_przeplywu(False)
                app.btn5.setText("Wznow")
            else:
                app.timer5.start(20)
                app.btn5.setText("Zatrzymaj")
            app.running5 = not app.running5
            app.update()
        elif nr_procesu == 6:
            if app.running6:
                app.timer6.stop()
                app.r7.ustawienie_przeplywu(False)
                app.btn6.setText("Wznow")
            else:
                app.timer6.start(20)
                app.btn6.setText("Zatrzymaj")
            app.running6 = not app.running6
            app.update()
        elif nr_procesu == 7:
            if app.running7:
                app.timer7.stop()
                app.r10.ustawienie_przeplywu(False)
                app.btn7.setText("Wznow")
            else:
                app.timer7.start(20)
                app.btn7.setText("Zatrzymaj")
            app.running7 = not app.running7
            app.update()
        elif nr_procesu == 8:
            if app.running8:
                app.timer8.stop()
                app.r11.ustawienie_przeplywu(False)
                app.btn8.setText("Wznow")
            else:
                app.timer8.start(20)
                app.btn8.setText("Zatrzymaj")
            app.running8 = not app.running8
            app.update()
        elif nr_procesu == 9:
            if app.running9:
                app.timer9.stop()
                app.btn9.setText("Wznow")
            else:
                app.timer9.start(20)
                app.btn9.setText("Zatrzymaj")
            app.running9 = not app.running9
            app.update()
        elif nr_procesu == 10:
            if app.running10:
                app.timer10.stop()
                app.btn10.setText("Wznow")
                app.r10.ustawienie_przeplywu(False)
                app.r11.ustawienie_przeplywu(False)
            else:
                app.running3 = False
                app.timer3.stop()
                app.btn3.setText("Otworz")
                for r in [app.r1, app.r2, app.r3, app.r4]:
                    r.ustawienie_przeplywu(False)
                app.running5 = False
                app.timer5.stop()
                app.btn5.setText("Pompuj")
                app.r9.ustawienie_przeplywu(False)
                app.running6 = False
                app.timer6.stop()
                app.btn6.setText("Pompuj")
                app.r7.ustawienie_przeplywu(False)
                app.timer10.start(20)
                app.btn10.setText("Zatrzymaj")
            app.running10 = not app.running10
            app.update()
            
        elif nr_procesu == 11:
            if app.running11:
                app.timer11.stop()
                app.btn11.setText("Wznow")
            else:
                app.timer11.start(20)
                app.btn11.setText("Zatrzymaj")
            app.running11 = not app.running11
            app.update()
            
        elif nr_procesu == 12:
            if app.running12:
                app.timer12.stop()
                app.btn12.setText("Wznow")
            else:
                app.timer12.start(20)
                app.btn12.setText("Zatrzymaj")
            app.running12 = not app.running12
            app.update()

    def pompowanie_cieczy(nr_procesu):
        pompowanie = False
        if nr_procesu == 1:
            if not app.z1.czy_pelny():
                total = app.z1.aktualna_ilosc + 2
                if total > 0:
                    app.z1.temp = (app.z1.aktualna_ilosc * app.z1.temp) / total
                app.z1.dodaj_ciecz(2)
                pompowanie = True
                app.r5.ustawienie_przeplywu(pompowanie)
            else:
                app.r5.ustawienie_przeplywu(False)
        elif nr_procesu == 2:
            if not app.z2.czy_pelny():
                total = app.z2.aktualna_ilosc + 2
                if total > 0:
                    app.z2.temp = (app.z2.aktualna_ilosc * app.z2.temp) / total
                app.z2.dodaj_ciecz(2)
                pompowanie = True
                app.r6.ustawienie_przeplywu(pompowanie)
            else:
                app.r6.ustawienie_przeplywu(False)
        elif nr_procesu == 3:
            if not app.z3.czy_pelny():
                total = app.z3.aktualna_ilosc + 2
                if total > 0:
                    app.z3.temp = (app.z3.aktualna_ilosc * app.z3.temp) / total
                app.z3.dodaj_ciecz(2)
                pompowanie = True
                app.r8.ustawienie_przeplywu(pompowanie)
            else:
                app.r8.ustawienie_przeplywu(False)
        elif nr_procesu == 4:
            if not app.z4.czy_pelny():
                total = app.z4.aktualna_ilosc + 2
                if total > 0:
                    app.z4.temp = (app.z4.aktualna_ilosc * app.z4.temp) / total
                app.z4.dodaj_ciecz(2)
                pompowanie = True
                app.r9.ustawienie_przeplywu(pompowanie)
            else:
                app.r9.ustawienie_przeplywu(False)
        elif nr_procesu == 5:
            if not app.z5.czy_pelny():
                total = app.z5.aktualna_ilosc + 2
                if total > 0:
                    app.z5.temp = (app.z5.aktualna_ilosc * app.z5.temp) / total
                app.z5.dodaj_ciecz(0.5)
                pompowanie = True
                app.r7.ustawienie_przeplywu(pompowanie)
            else:
                app.r7.ustawienie_przeplywu(False)
        app.update()

    def odpompowanie_cieczy(nr_procesu):
        odpompowanie = False
        if nr_procesu == 1:
            if app.z5.aktualna_ilosc > 0.5:
                app.z5.usun_ciecz(0.2)
                odpompowanie = True
                app.r10.ustawienie_przeplywu(odpompowanie)
            else:
                app.r10.ustawienie_przeplywu(False)
        elif nr_procesu == 2:
            if app.z4.aktualna_ilosc > 0.5:
                app.z4.usun_ciecz(0.2)
                odpompowanie = True
                app.r11.ustawienie_przeplywu(odpompowanie)
            else:
                app.r11.ustawienie_przeplywu(False)
        app.update()

    def podgrzewaj_z1():
        if app.z1.aktualna_ilosc > 0:
            app.z1.temp = min(100, app.z1.temp + 4)
            app.update()
            
    def dodaj_zimnej_z1():
        if app.z1.aktualna_ilosc > 0:
            app.z1.temp = max(0, app.z1.temp - 4)
            app.update()

    def reguluj_poziom():
        if app.running3:
            return
        roznica = app.z4.aktualna_ilosc - app.z5.aktualna_ilosc
        tolerancja = 0.5
        if abs(roznica) <= tolerancja:
            app.running10 = not app.running10
            app.timer10.stop()
            app.btn10.setText("Reguluj Poziom(Dolne Zbiorniki)")
            app.running7 = False
            app.timer7.stop()
            app.btn7.setText("Opompuj")
            app.running8 = False
            app.timer8.stop()
            app.btn8.setText("Opompuj")
            app.running5 = False
            app.timer5.stop()
            app.btn5.setText("Pompuj")
            app.r9.ustawienie_przeplywu(False)
            app.running6 = False
            app.timer6.stop()
            app.btn6.setText("Pompuj")
            app.r7.ustawienie_przeplywu(False)
            for r in [app.r3, app.r4, app.r6, app.r8, app.r10, app.r11]:
                r.ustawienie_przeplywu(False)
            app.update()
            return
        if roznica > 0:
            app.pompowanie_cieczy(5)
            app.odpompowanie_cieczy(2)
            app.running7 = False
            app.timer7.stop()
            app.btn7.setText("Odpompuj")
            app.r10.ustawienie_przeplywu(False)
        else:
            app.pompowanie_cieczy(4)
            app.odpompowanie_cieczy(1)
            app.running8 = False
            app.timer8.stop()
            app.btn8.setText("Odpompuj")
            app.r11.ustawienie_przeplywu(False)
        app.update()

    def wymus_przeplyw():
        out_speed = app.flow_speed / 2
        if app.z2.aktualna_ilosc > 0.1 and not app.z5.czy_pelny():
            wsad = app.z2.usun_ciecz(out_speed)
            total_woda = app.z5.aktualna_ilosc + wsad
            if total_woda > 0.2:
                nowa_temp = (app.z5.aktualna_ilosc * app.z5.temp + wsad * app.z2.temp) / total_woda
                app.z5.temp = nowa_temp
            app.z5.dodaj_ciecz(wsad)
            app.r3.ustawienie_przeplywu(True)
        else:
            app.r3.ustawienie_przeplywu(False)
        if app.z3.aktualna_ilosc > 0.1 and not app.z4.czy_pelny():
            wsad = app.z3.usun_ciecz(out_speed)
            total_woda = app.z4.aktualna_ilosc + wsad
            if total_woda > 0.2:
                nowa_temp = (app.z4.aktualna_ilosc * app.z4.temp + wsad * app.z3.temp) / total_woda
                app.z4.temp = nowa_temp
            app.z4.dodaj_ciecz(wsad)
            app.r4.ustawienie_przeplywu(True)
        else:
            app.r4.ustawienie_przeplywu(False)
            
    def reguluj_temperature():
        roznica = app.z4.temp - app.z5.temp
        tolerancja = 1
        if abs(roznica) <= tolerancja:
            app.running11 = False
            app.timer11.stop()
            app.btn11.setText("Reguluj Temperature(Dolne Zbiorniki)")
        if roznica > 1:
            app.z5.temp = min(100, app.z5.temp + 0.2)
            app.z4.temp = min(100, app.z4.temp - 0.2)
            app.running3 = False
            app.timer3.stop()
            app.btn3.setText("Otworz zawory")
            for r in [app.r1, app.r2, app.r3, app.r4]:
                r.ustawienie_przeplywu(False)
            app.running2 = False
            app.timer2.stop()
            app.btn2.setText("Pompuj")
            app.r6.ustawienie_przeplywu(False)
            app.running8 = False
            app.timer8.stop()
            app.btn8.setText("Odpompuj")
            app.r11.ustawienie_przeplywu(False)
            app.running4 = False
            app.timer4.stop()
            app.btn4.setText("Pompuj")
            app.r8.ustawienie_przeplywu(False)
            app.running7 = False
            app.timer7.stop()
            app.btn7.setText("Odpompuj")
            app.r10.ustawienie_przeplywu(False)
            app.running5 = False
            app.timer5.stop()
            app.btn5.setText("Pompuj")
            app.r7.ustawienie_przeplywu(False)
            app.running6 = False
            app.timer6.stop()
            app.btn6.setText("Pompuj")
            app.r9.ustawienie_przeplywu(False)
            app.update()
        else:
            app.z4.temp = min(100, app.z4.temp + 0.2)
            app.z5.temp = min(100, app.z5.temp - 0.2)
            app.running3 = False
            app.timer3.stop()
            app.btn3.setText("Otworz zawory")
            for r in [app.r1, app.r2, app.r3, app.r4]:
                r.ustawienie_przeplywu(False)
            app.running2 = False
            app.timer2.stop()
            app.btn2.setText("Pompuj")
            app.r6.ustawienie_przeplywu(False)
            app.running8 = False
            app.timer8.stop()
            app.btn8.setText("Odpompuj")
            app.r11.ustawienie_przeplywu(False)
            app.running4 = False
            app.timer4.stop()
            app.btn4.setText("Pompuj")
            app.r8.ustawienie_przeplywu(False)
            app.running7 = False
            app.timer7.stop()
            app.btn7.setText("Odpompuj")
            app.r10.ustawienie_przeplywu(False)
            app.running5 = False
            app.timer5.stop()
            app.btn5.setText("Ppompuj")
            app.r7.ustawienie_przeplywu(False)
            app.running6 = False
            app.timer6.stop()
            app.btn6.setText("Pompuj")
            app.r9.ustawienie_przeplywu(False)
            app.update()

    def logika_przeplywu():
        out_speed = app.flow_speed / 2 
        plynie_1 = False
        plynie_2 = False
        if app.z1.aktualna_ilosc > 0.1:
            if not app.z2.czy_pelny():
                wsad = app.z1.usun_ciecz(out_speed)
                total_woda = app.z2.aktualna_ilosc + wsad
                if total_woda > 0.2:
                    nowa_temp = (app.z2.aktualna_ilosc * app.z2.temp + wsad * app.z1.temp) / total_woda
                    app.z2.temp = nowa_temp
                app.z2.dodaj_ciecz(wsad)
                plynie_1 = True
            if not app.z3.czy_pelny():
                wsad = app.z1.usun_ciecz(out_speed)
                total_woda = app.z3.aktualna_ilosc + wsad
                if total_woda > 0.2:
                    nowa_temp = (app.z3.aktualna_ilosc * app.z3.temp + wsad * app.z1.temp) / total_woda
                    app.z3.temp = nowa_temp
                app.z3.dodaj_ciecz(wsad)
                plynie_2 = True
        app.r1.ustawienie_przeplywu(plynie_1)
        app.r2.ustawienie_przeplywu(plynie_2)
        plynie_3 = False
        if app.z2.aktualna_ilosc > 0.1 and not app.z5.czy_pelny():
            wsad = app.z2.usun_ciecz(out_speed)
            total_woda = app.z5.aktualna_ilosc + wsad
            if total_woda > 0.2:
                nowa_temp = (app.z5.aktualna_ilosc * app.z5.temp + wsad * app.z2.temp) / total_woda
                app.z5.temp = nowa_temp
            app.z5.dodaj_ciecz(wsad)
            plynie_3 = True
        app.r3.ustawienie_przeplywu(plynie_3)
        plynie_4 = False
        if app.z3.aktualna_ilosc > 0.1 and not app.z4.czy_pelny():
            wsad = app.z3.usun_ciecz(out_speed)
            total_woda = app.z4.aktualna_ilosc + wsad
            if total_woda > 0.2:
                nowa_temp = (app.z4.aktualna_ilosc * app.z4.temp + wsad * app.z3.temp) / total_woda
                app.z4.temp = nowa_temp
            app.z4.dodaj_ciecz(wsad)
            plynie_4 = True
        app.r4.ustawienie_przeplywu(plynie_4)  
        app.update()

    app.przelacz_symulacje = przelacz_symulacje
    app.pompowanie_cieczy = pompowanie_cieczy
    app.odpompowanie_cieczy = odpompowanie_cieczy
    app.podgrzewaj_z1 = podgrzewaj_z1
    app.reguluj_poziom = reguluj_poziom
    app.wymus_przeplyw = wymus_przeplyw
    app.logika_przeplywu = logika_przeplywu

    app.flow_speed = 0.8
    
    app.timer1 = QTimer()
    app.timer1.timeout.connect(lambda: app.pompowanie_cieczy(1))
    app.btn1 = QPushButton("Pompuj", app)
    app.btn1.setGeometry(475, 10, 80, 30)
    app.btn1.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn1.clicked.connect(lambda: app.przelacz_symulacje(1))
    app.running1 = False
    
    app.timer2 = QTimer()
    app.timer2.timeout.connect(lambda: app.pompowanie_cieczy(2))
    app.btn2 = QPushButton("Pompuj", app)
    app.btn2.setGeometry(10, 325, 80, 30)
    app.btn2.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn2.clicked.connect(lambda: app.przelacz_symulacje(2))
    app.running2 = False
    
    app.timer3 = QTimer()
    app.timer3.timeout.connect(app.logika_przeplywu)
    app.btn3 = QPushButton("Otworz zawory", app)
    app.btn3.setGeometry(10, 10, 120, 30)
    app.btn3.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn3.clicked.connect(lambda: app.przelacz_symulacje(3))
    app.running3 = False
    
    app.timer4 = QTimer()
    app.timer4.timeout.connect(lambda: app.pompowanie_cieczy(3))
    app.btn4 = QPushButton("Pompuj", app)
    app.btn4.setGeometry(790, 325, 80, 30)
    app.btn4.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn4.clicked.connect(lambda: app.przelacz_symulacje(4))
    app.running4 = False
    
    app.timer5 = QTimer()
    app.timer5.timeout.connect(lambda: app.pompowanie_cieczy(4))
    app.btn5 = QPushButton("Pompuj", app)
    app.btn5.setGeometry(790, 485, 80, 30)
    app.btn5.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn5.clicked.connect(lambda: app.przelacz_symulacje(5))
    app.running5 = False
    
    app.timer6 = QTimer()
    app.timer6.timeout.connect(lambda: app.pompowanie_cieczy(5))
    app.btn6 = QPushButton("Pompuj", app)
    app.btn6.setGeometry(10, 485, 80, 30)
    app.btn6.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn6.clicked.connect(lambda: app.przelacz_symulacje(6))
    app.running6 = False
    
    app.timer7 = QTimer()
    app.timer7.timeout.connect(lambda: app.odpompowanie_cieczy(1))
    app.btn7 = QPushButton("Odpompuj", app)
    app.btn7.setGeometry(274, 610, 80, 30)
    app.btn7.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn7.clicked.connect(lambda: app.przelacz_symulacje(7))
    app.running7 = False
    
    app.timer8 = QTimer()
    app.timer8.timeout.connect(lambda: app.odpompowanie_cieczy(2))
    app.btn8 = QPushButton("Odpompuj", app)
    app.btn8.setGeometry(534, 610, 80, 30)
    app.btn8.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn8.clicked.connect(lambda: app.przelacz_symulacje(8))
    app.running8 = False
    
    app.timer9 = QTimer()
    app.timer9.timeout.connect(lambda: app.podgrzewaj_z1())
    app.btn9 = QPushButton("Podgrzej", app)
    app.btn9.setGeometry(410, 260, 80, 30)
    app.btn9.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn9.clicked.connect(lambda: app.przelacz_symulacje(9))
    app.running9 = False
    
    app.timer10 = QTimer()
    app.timer10.timeout.connect(lambda: app.reguluj_poziom())
    app.btn10 = QPushButton("Reguluj Poziom(Dolne Zbiorniki)", app)
    app.btn10.setGeometry(10, 50, 200, 30)
    app.btn10.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn10.clicked.connect(lambda: app.przelacz_symulacje(10))
    app.running10 = False
    
    app.timer11 = QTimer()
    app.timer11.timeout.connect(lambda: reguluj_temperature())
    app.btn11 = QPushButton("Reguluj Temperature(Dolne Zbiorniki)", app)
    app.btn11.setGeometry(10, 90, 230, 30)
    app.btn11.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn11.clicked.connect(lambda: app.przelacz_symulacje(11))
    app.running11 = False
    
    app.timer12 = QTimer()
    app.timer12.timeout.connect(lambda: dodaj_zimnej_z1())
    app.btn12 = QPushButton("Ochlodz", app)
    app.btn12.setGeometry(410, 300, 80, 30)
    app.btn12.setStyleSheet("background-color: #444; color: white; font-weight: bold;")
    app.btn12.clicked.connect(lambda: app.przelacz_symulacje(12))
    app.running12 = False
    



