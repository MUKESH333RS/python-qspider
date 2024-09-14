# 54.	Write a program to check the relation between two integer numbers
num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
if num1 == num2:
    print(f"The two number {num1} and {num2} is equal.")
elif num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
elif num1 < num2:
    print(f"{num1} is lesser than {num2}.")
elif num2 < num1:
    print(f"{num2} is lesser than {num1}.")
else:
    print(f"There is no relation between {num1} and {num2}.")

