#nejvetsi spolecny delitel
cislo1 = int(input('Zadej cislo 1: '))
cislo2 = int(input('Zadej cislo 2: '))

def deleni(cislo):

    delitele = []
    for i in range(1, cislo+1):
        if cislo % i == 0:
            delitele.append(i)

    return(delitele)

delitele1 = deleni(cislo1)
delitele2 = deleni(cislo2)

print(delitele1)
print(delitele2)

spolecni = []

for prvek in delitele1:
    if prvek in delitele2:
        spolecni.append(prvek)

print(spolecni)

print('Nejvetsi spolecny delitel je: ', max(spolecni))
