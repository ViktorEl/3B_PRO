
pocet_kusov = input('Zadajte pocet kusov:')
pocet_kusov = int(pocet_kusov)

for i in range(10, pocet_kusov+1, 10):
    vypocet = i * 12
    print(f'{i} kusov = {vypocet}')