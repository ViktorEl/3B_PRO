
od_cisla = input('Zadajte od akeho cisla chcete vypocitat mocniny:')
od_cisla = int(od_cisla)


do_cisla = input('zadajte do akeho cisla chcete vypocitat mocniny:')
do_cisla = int(do_cisla)



for i in range(od_cisla, do_cisla+1):
    mocnina = i**2
    print(f'Druhá mocnina cisla {i} je {mocnina}')
