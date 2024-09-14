# 22.	Write a program to check whether the given character is digit

digit = input("Enter a digit:")
if digit.isnumeric():
    print(f"The given character {digit} is digit.")

# another method
if '0' <= digit <='9':
    print(f"The given character {digit} is digit.")