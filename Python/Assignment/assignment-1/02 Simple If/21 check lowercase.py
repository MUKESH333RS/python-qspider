# 21.	Write a program.To check whether the given character is lowercase alphabet

char = input("Enter a character:")
if char.islower():
    print(f"The given character {char} is lowercase alphabet.")

# another method
if 'a' <= char <= 'z':
    print(f"The given character {char} is lowercase alphabet.")