"""
read a character
set vowels as aeiou

display vowel if char in vowel

display not vowel otherwise

"""

character = input("enter characetr ")

VOWELS = "aeiou"

if character in VOWELS:

    print("vowel")

else:

    print("not vowel")