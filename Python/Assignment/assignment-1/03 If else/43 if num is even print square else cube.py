# 43.	Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.

num = int(input("Enter a integer number:"))
if num % 2 == 0:
    print(f"The square of the number is:{num ** 2}")
else:
    print(f"The cube of the number is:{num ** 3}")