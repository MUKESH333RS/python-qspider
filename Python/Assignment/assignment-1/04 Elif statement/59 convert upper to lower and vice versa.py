# 59.	Write a program to check whether given character is uppercase, print its lowercase character or if given character is lowercase print its uppercase character or if given character is special character print the character after adding 8 to the ascii value of that particle special character.

char = input("enter a character:")
if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
else:
    print(chr(ord(char) + 8))