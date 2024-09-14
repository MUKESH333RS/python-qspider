# 55.	Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it.

char = input("Enter a number:")
if char.isupper():
    print("uppercase")
elif char.islower():
    print("lowercase")
elif char.isnumeric():
    print(ord(char))