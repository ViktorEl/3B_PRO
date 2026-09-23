# Pomocou meracieho pásma sme odmerali rozmery 
# telocvične: šírka 15 m a 32 cm, dĺžka 22 m a 12 cm. 
# Koľko plechoviek farby budeme potrebovať 
# na premaľovanie podlahy telocvične, 
# ak farba z jednej plechovky vystačí na 14 m2?

import math

sirka = 15.32
dlzka = 22.12
obsah = sirka * dlzka
plechovka = 14


plechovky_spolu = obsah / plechovka
plechovky_spolu = math.ceil(plechovky_spolu)

print(plechovky_spolu)
