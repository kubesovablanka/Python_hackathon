#!/usr/bin/env python3

# define a function to load the dictionary to internal structure
# we will load it from external file
#def load_dict():
#    pass

# process the input word we're working with

# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagram

zadani = input('Zadej slovo: ')
input_serazeni = sorted(zadani)
print(input_serazeni)
input_final = ''.join(input_serazeni)
print(input_final)

dictionary = open('slovnik.txt')
obsah = dictionary.readlines()     #readlines vraci radky

#print(obsah)
pozice = []
for slovo in obsah:
    item = slovo.split("\n")
    item = sorted(item)
    final = ''.join(item)
    #print(final)
    if sorted(final) == sorted(input_final):
        pozice.append(final)

print('Anagrams of input word are:', pozice)

dictionary.close()
