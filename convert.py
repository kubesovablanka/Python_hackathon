number = int(input('Zadej cislo, ktere chces prevest: '))
base = int(input('Zadej soustavu, do ktere chces prevadet: '))

#cislice = '0123456789abcdef'

def convert(number, base):
    cislice = '0123456789abcdef'
    #number = int(input("Enter decimal number you want convert: "))
    output = ""

    while number > 0:
        print('number = ', number,'   output = ', output) # this will help you keep track content of variable
        index = number % base
        output = cislice[index] + output
        number = int(number / base)

    popis = ''
    if base == 2:
        popis = '0b'
    elif base == 16:
        popis = '0x'
    else:
        popis = ''


    
    print('Input number converted is : ', popis + output)

convert(number, base)
