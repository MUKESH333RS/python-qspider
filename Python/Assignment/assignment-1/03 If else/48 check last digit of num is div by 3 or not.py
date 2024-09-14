# 48.	Write a program to check whether the last digit of a number entered by the user is divisible by three or not.

num = int(input("Enter a number:"))
last_digit = num % 10
if last_digit % 3 == 0:
    print(f"The last digit {last_digit} of a number {num} is divisible by 3.")
else:
    print(f"The last digit {last_digit} of a number {num} is not divisible by 3.")

