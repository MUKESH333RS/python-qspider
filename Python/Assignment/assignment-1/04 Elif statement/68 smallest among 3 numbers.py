# 68.	Write a program to find the smallest among three numbers

num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
num3 = int(input("Enter a number3:"))
if num1 < num2 and num1 < num3:
    print(f"{num1} is smallest.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} is smallest.")
else:
    print(f"{num3} is smallest.")