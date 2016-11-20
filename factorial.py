# #factorial
# cislo = int(input('Zadej cislo: '))
# print(cislo)
#
# faktorial = 1
# for i in range(cislo):
#     faktorial *= (i+1)
#
# print(faktorial)

#factorial rekursivne
cislo = int(input('Zadej cislo: '))

def faktorial(cislo):

    if cislo > 1:
        return faktorial(cislo-1) * cislo
    else:
        return 1

print(faktorial(cislo))
