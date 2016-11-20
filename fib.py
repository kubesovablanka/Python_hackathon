#fibonacci

# cislo = int(input('Zadej pocet clenu, který chces vypsat: '))
#
# a,b = 0,1
# for i in range(cislo):
#     a,b = b,a+b
#
# print (a)

#fibonacci rekursivne
pozice = int(input('Zadej pozici: '))

def fib(pozice):
    if pozice > 2:
        return fib(pozice-1) + fib(pozice-2)
    elif pozice == 0:
        return 0
    else:
        return 1

print(fib(pozice))
