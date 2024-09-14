# 24.	Write a program to check whether the given character is a special character

char = input("Enter a special character:")
if char.isalnum() == False:
    print(f"The given character {char} is a special character.")