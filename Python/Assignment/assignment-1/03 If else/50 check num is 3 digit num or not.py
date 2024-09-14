# 50.	Write a program to check whether a number entered is a 3 digit number or not.

num = int(input("Enter a number:"))
if -999 <= num <= 999:
    print(f"The number {num} is a 3 digit number.")
else:
    print(f"The number {num} is not a 3 digit number.")