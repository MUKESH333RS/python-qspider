# 61.	Write a program to check if the middle value of heterogeneous tuple collection is integer or not.
tuple1 = eval(input("Enter a number:"))
mid_value = (len(tuple1) - 1) // 2
if type(mid_value) == int:
    print(f"The middle value {mid_value} of heterogeneous tuple collection is integer.")
else:
    print(f"The middle value {mid_value} of heterogeneous tuple collection is not integer.")