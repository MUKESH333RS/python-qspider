# 63.	write a program to check whether the given integer single digit or two digits or three digits or more than three digits

digit = int(input("Enter a digit:"))
if -9 <= digit <= 9:
    print(f"The given data {digit} has a single digit.")
elif -99 <= digit <= 99:
    print(f"The given data {digit} has a two digits.")
elif -999 <= digit <= 999:
    print(f"The given data {digit} has a three digits.")
else:
    print(f"The given data {digit} has a more than three digits.")