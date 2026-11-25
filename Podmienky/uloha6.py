
vyska = input('Zadajte vysku v cm:')
vyska = float(vyska)
pohlavie = input('Zadajte pohlavie chlapec/dievca:')

if pohlavie == 'chlapec':
    if vyska < 160:
        print('futbal')
    elif vyska <= 175:
        print('vodne polo')
    elif vyska > 175:
        print('basketbal')
if pohlavie == 'dievca':
    if vyska < 160:
        print('akvabely')
    elif vyska <= 175:
        print('tenis')
    elif vyska > 175:
        print('volejbal')


