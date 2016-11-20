
def decimal_to_bin():

    number = int(input("Enter decimal number you want convert to binary: "))
    output = ""

    while number > 0:
        print('number = ', number,'   output = ', output) # this will help you keep track content of variable
        if number % 2 == 0:
            output = '0' + output
            number = int(number / 2)
        else:
            output = '1' + output
            number = int(number / 2)


    print('Input number converted to binary is : ',output)

decimal_to_bin()
