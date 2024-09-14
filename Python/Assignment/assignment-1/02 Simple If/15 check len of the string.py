# 15.	Write a program To check whether the given string is having more than three characters

string = input("Enter a String:")
length = len(string)
if length > 3:
    print(f"The given string {string} is more than three characters.")