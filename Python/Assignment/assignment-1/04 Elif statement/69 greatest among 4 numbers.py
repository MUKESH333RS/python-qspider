# 69.	Write a program to find the greatest among four numbers.	Write a program to find the greatest among four numbers

num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
num3 = int(input("Enter a number3:"))
num4 = int(input("Enter a number4:"))
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is greatest.")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is greatest.")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is greatest.")
else:
    print(f"{num4} is greatest.")