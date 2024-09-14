# 29.	Write a program to check whether the entered input is.Immutable.

collection = eval(input("Enter a collection:"))
if type(collection) in (str,tuple):
    print(f"The collection {collection} is Immutable.")