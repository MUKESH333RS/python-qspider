# 51.	Write a program to find the largest number out of two numbers expected from the user.

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
if num1 > num2:
    print(f"{num1} is a largest number.")
else:
    print(f"{num2} is a largest number.")