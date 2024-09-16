# 66. Write a program to check whether the entered character is uppercase or lowercase or number or special character

char = input("Enter a number:")
if char.isupper():
    print(f"The entered character {char} is uppercase")
elif char.islower():
    print(f"The entered character {char} is lowercase")
elif char.isnumeric():
    print(f"The entered character {char} is number.")
else:
    print(f"The entered character {char} is special character.")