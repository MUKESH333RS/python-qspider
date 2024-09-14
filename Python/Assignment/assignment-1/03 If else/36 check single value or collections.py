# 36.	Write a program to check whether the given data is single value or collection.

data = eval(input("Enter a value or collection:"))
if type(data) in (int,float,complex,bool):
    print(f"The given data {data} is single value data type")
else:
    print(f"The given data {data} is collection")