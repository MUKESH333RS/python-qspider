# 26.	Write a program to check whether the entered value is default

value = eval(input("Enter a value:"))
if bool(value) == False:
    print(f"The entered value {value} is default")