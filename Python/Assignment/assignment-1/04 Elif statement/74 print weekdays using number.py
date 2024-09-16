# 74.	Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.

num = int(input("Enter a number to print weekdays:"))
weekdays = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}

if num <= 7:
    print(f"The weekday of number {num} is {weekdays[num]}.")
else:
    print("Enter a valid number.")