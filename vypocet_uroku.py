#Vytvorte program, ktorý si od používateľa vypýta vklad 
# a úrokovú mieru v % a vypočíta a vypíše zisk z úroku 
# za jednej rok aj celkovú sumu peňazí po jednom roku. 
#Pomôcka: použite formátovaný string / fstring
#f'Zisk z uroku = {nazov_premennej1} 
# a celkova suma = {nazov_premennej2}'

vklad = input('Zadajte svoj vklad:')
vklad = float(vklad)

urok_v_percentach = input('Zadajte urokovu mieru v %:')
urok_v_percentach = float(urok_v_percentach)

zisk_z_uroku = (urok_v_percentach / 100) * vklad 
celkova_suma = zisk_z_uroku + vklad

print(f'Váš zisk je {urok_v_percentach} € s celkovou sumou {celkova_suma} €')