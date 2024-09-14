# 38.	Write a program to check whether the given string is having the middle character or not.

string = input("Enter a string:")
if len(string) % 2 == 0:
    print(f"The string {string} is not having the middle character.")
else:
    print(f"The string {string} is having the middle character.")