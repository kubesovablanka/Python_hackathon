# -*- coding: utf-8 -*-

#--------------------skeleton of credit card validator--------------------
#The credit card number we want to validate. This program works with *most* credit card numbers.

#card_number = str(input("Enter credit card number you want to check: "))
#card_number = '4012888888881881'
card_number = '5168342160909548'

# Reverse the credit card number and take the digits in the odd positions and then the digits in the even positions
#
# Add up all the digits in the odd positions into a total.
#
# Multiply every even-positioned digit by two;
#   if the product is greater than 9 (e.g. 8 * 2 = 16),
#      then subtract 9 and add the result to the total.
#   Otherwise add the multiplication product to the total.
#
# If the total is divisible by 10 (the remainder after division by 10 is equal to 0 or the number ends in a zero);
#   then the credit card number is valid.


reversed_card_number = card_number[::-1]
even_digits = reversed_card_number[1::2]
odd_digits = reversed_card_number[0::2]


total = 0
for digit in odd_digits: # add up all odd digits
    total += int(digit)

for digit in even_digits: # for every even digit
    multiplied = int(digit) * 2
    if multiplied > 9:
        result = multiplied - 9
        total += result
    else:
        total += multiplied

print(total)

# Now that we have the sum, we can create a checksum
checksum = total % 10

print(card_number)
if checksum == 0: # If the remainder of the total is 0 (total is divisible by 10)
    print('Valid!')
else:
    print('Your credit card number is not valid. Please check for any typos.')
