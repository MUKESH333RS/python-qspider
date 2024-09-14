# 46.	Write a program to check whether the user is eligible to vote or not.

user_age = int(input("Enter your age:"))
if user_age >= 18:
    print("you are eligible for vote.")
else:
    print("you are not eligible for vote.")