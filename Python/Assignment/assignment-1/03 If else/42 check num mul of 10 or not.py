# 42.	Write a program to check whether the given integer number is multiple of 10 or not.
num = int(input("Enter a number:"))
if num % 10 == 0:
    print(f"The given integer number {num} is multiple of 10.")
else:
    print(f"The given integer number {num} is not multiple of 10.")