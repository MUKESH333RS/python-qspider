# 31.	Write a program to check whether The entered input is a single value

value = eval(input("Enter a value or collection:"))
if type(value) in (int,float,complex,bool):
    print(f"The entered input {value} is single value data type.")