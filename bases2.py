def bin_to_decimal():

    binary = input("Enter binary number you want convert to decimal: ")
    decimal = 0

    for digit in binary:    #you can iterate through binary string

        print('digit:', digit, 'decimal:', decimal)
        decimal = decimal * 2 + int(digit)

    print(binary, 'converted to decimal is:', decimal)

bin_to_decimal()
