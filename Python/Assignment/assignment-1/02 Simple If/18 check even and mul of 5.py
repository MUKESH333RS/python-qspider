# 18.	Write a program to check whether the given integer number is even and multiple of five

num = int(input("Enter a number:"))
if num % 2 == 0 and num % 5 == 0:
    print(f"The given number {num} is even and multiple of 5.")