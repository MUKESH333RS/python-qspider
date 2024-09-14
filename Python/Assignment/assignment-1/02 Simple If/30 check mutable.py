# 30.	Write a program to check whether the entered input is mutable.

collection = eval(input("Enter a collection:"))
if type(collection) in (list,set,dict):
    print(f"The entered collection {collection} is Mutable.")