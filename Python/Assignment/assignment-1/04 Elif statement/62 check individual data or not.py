# 62.	Write a program to check if the given data is individual data type or not.

data = eval(input("Enter a data:"))
if type(data) in (int,float,bool,str):
    print(f"The given data {data} is an individual data.")
else:
    print(f"The given data {data} is not an individual data.")
