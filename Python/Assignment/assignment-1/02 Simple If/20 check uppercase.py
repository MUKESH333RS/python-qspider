# 20.	Write a program.To check whether the given character is uppercase alphabet

char = input("Enter a character:")
if char.isupper():
    print(f"The given character {char} is uppercase alphabet.")

# another method
if 'A' <= char <= 'Z':
    print(f"The given character {char} is uppercase alphabet.")