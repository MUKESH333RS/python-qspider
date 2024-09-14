# 27.	Write a program to check whether The list consists of even number of values

list1 = eval(input("Enter a list:"))
sum_of_list = sum(list1)
if sum_of_list % 2 == 0:
    print(f"The list {list1} consists of even number of values.")