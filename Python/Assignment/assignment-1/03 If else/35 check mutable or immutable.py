# 35.	Write a program to check whether the given data is mutable or immutable.

collection = eval(input("Enter a collection:"))
if type(collection) in (str,tuple):
    print(f"The given data {collection} is Immutable.")
else:
    print(f"The given data {collection} is Mutable.")