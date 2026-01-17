from rura import Rura
from zbiornik import Zbiornik

def moje_elementy_graficzne(self):
    #Rury
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
    #Zbiorniki
    self.z1 = Zbiornik(294,50,300,180, "ZBIORNIK 1")
    self.z2 = Zbiornik(124,330, 120, 80, "ZBIORNIK 2")
    self.z3 = Zbiornik(644,330, 120, 80, "ZBIORNIK 3")
    self.z4 = Zbiornik(524,490, 120, 80, "ZBIORNIK 5")
    self.z5 = Zbiornik(244,490, 120, 80, "ZBIORNIK 4")

