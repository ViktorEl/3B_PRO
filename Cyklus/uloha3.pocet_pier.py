
pocet_pier = input('Zadajte pocet pier:')
pocet_pier = int(pocet_pier)

for i in range(1, pocet_pier + 1):
    cena = i * 1.50
    print(f'{i} kus = {cena}')
