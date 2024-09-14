# 40.	Write a program to check whether the first value present inside the given list is complex or not.
list1 = eval(input("Enter a list:"))
first_value = list1[0]
if type(first_value) == complex:
    print(f"The first value {first_value} present inside the given list is complex.")
else:
    print(f"The first value {first_value} present inside the given list is  not complex.")
