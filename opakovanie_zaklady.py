# kalkulacka na scítanie
# kalkulacka si vypýta od pouzivatela dve cisla
# a pomocou formatovaneho retazca vypise vysledok
# vysledok vypiste vo formate cislo1 + cislo2 = vysledok

print('Vitajte, mozete vyuzit nasu kalkulacku na scitanie')

cislo1 = input('Prosím zadajte prve cislo:') # pozor input vracia string(retazec)
cislo1 = float(cislo1) # pretypovanie zo stringu na desatinne cislo

cislo2 = float(input('Zadajte druhé cislo:')) # druha moznost pretypovanie priamo bez pomocneho riadku

vysledok = cislo1 + cislo2
print(f'{cislo1} + {cislo2} = {vysledok}') # {tieto zatvorky sa robia skratkou pravy altGr + b}