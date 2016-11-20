import obrazky
from random import choice

#globalni promenne - nesmi byt pouzite nikde jako lokalni, pak by byl zmatek
soubor = open('tajenky.txt')
soubor_read = soubor.read()
tajenky = soubor_read.split('\n')    #precety soubor rozdeli posle \n (noveho radku)
tajenky = tajenky[:-1]               #urizne posledni prvek - prazdny retezec, ktery vytvari muj editor
hadane_slovo = choice(tajenky)

soubor.close()

def zamen(slovo, pozice, pismeno):
    "Vrati slovo se zamenenym pismenem na dane pozici"
    return slovo[:pozice] + pismeno + slovo[pozice+1:]

def vyhodnot(slovo):
    "Vyhodnoti pocet volnych mist ve slove"
    if '-' not in slovo:
        return('!')

def sibenice():
    "Prubeh tahu hrace"
    neuspesnych_pokusu = 0
    slovo = '-' * len(hadane_slovo)

    while True:
        pismeno = input('Zadej pimeno: ')

        if len(pismeno) > 1:
            print('Zadavej vzdy jen jedno pismeno')

        if len(pismeno) < 1:
            print('Musis neco zadat')
            continue

        if pismeno in slovo:
            print('Toto pismeno uz jsi hadal')

        elif pismeno in hadane_slovo:
                pozice = hadane_slovo.index(pismeno)
                slovo = zamen(slovo, pozice, pismeno)
                while pismeno in hadane_slovo[pozice+1:]:
                    pozice = hadane_slovo.index(pismeno, pozice + 1)
                    slovo = zamen(slovo, pozice, pismeno)

                print(slovo)
                if vyhodnot(slovo) == '!':
                    print('Gratulujeme!')
                    break

        else:
            neuspesnych_pokusu = neuspesnych_pokusu + 1
            print('Toto pismeno ve slove neni.')
            print(obrazky.spatny_pokus[neuspesnych_pokusu - 1])
            print(slovo)
            if neuspesnych_pokusu == 10:
                print('Bohuzel :-)')
                break
