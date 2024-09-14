# 41.	Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.

tuple1 = eval(input("Enter a tuple has only two values:"))
if type(tuple1[0]) == type(tuple1[1]):
    print(f"The tuple {tuple1} is homogenous.")
else:
    print(f"the tuple {tuple1} is heterogeneous.")