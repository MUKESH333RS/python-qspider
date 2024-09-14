# 39.	Write a program to check whether the given 2 variables are pointing to the same memory location or not.

var1 = eval(input("Enter a value1:"))
var2 = eval(input("Enter a value2:"))
if id(var1) == id(var2):        # Alternate method - if var1 is var2
    print(f"The given two variables {var1},{var2} are pointing same memory location.")
else:
    print(f"The given two variables {var1},{var2} are not pointing same memory location.")