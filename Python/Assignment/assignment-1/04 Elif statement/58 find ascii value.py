# 58.	Write a program to checkWhether the entered character is a number. If it is a number, print the ASCII value of that number.

char = input("Enter a character:")
if char.isnumeric():
    print(ord(char))