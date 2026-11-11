
pocet_rokov = input('Zadajte pocet rokov:')
pocet_rokov = int(pocet_rokov)

aktualny_rok = 1000 * 1.03
print(aktualny_rok)
for i in range(1, pocet_rokov):
    dalsi_rok = aktualny_rok * 1.03
    dalsi_rok = round(dalsi_rok, 2)
    print(dalsi_rok)
    aktualny_rok = dalsi_rok

