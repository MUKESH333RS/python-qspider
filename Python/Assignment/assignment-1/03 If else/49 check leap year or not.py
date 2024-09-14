# 49.	Write a program to check whether the year is leap year or not.

year = int(input("Enter an year:"))
if year % 4 == 0:
    print(f"The year {year} is leap year.")
else:
    print(f"The year {year} is not leap year.")