# 32.	Write a program to check whether the entered input is multivalue or not.

value = eval(input("Enter a value or collection:"))
if type(value) in (str,list,tuple,set,dict):
    print(f"The entered input {value} is multi-value data type.")
