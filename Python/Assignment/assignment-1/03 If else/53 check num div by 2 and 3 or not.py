# 53.	Write a program.To check whether a number accepted from the user is divisible by two and three both.

num = int(input("Enter a number:"))
if num % 2 == 0 and num % 3 == 0:
    print(f"The number {num} is divisible by both 2 and 3.")
else:
    print(f"The number {num} is not divisible by both 2 and 3.")