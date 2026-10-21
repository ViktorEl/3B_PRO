
velkobalenie = 12
pocet_kusov = input('Zajdate pocet kusov na sklade:')
pocet_kusov = int(pocet_kusov)

balenia = pocet_kusov // velkobalenie
zostane_na_sklade = pocet_kusov % velkobalenie

print(f'Vieme vytvorit {balenia} baleni.\nNa sklade zostane {zostane_na_sklade} kusov ')