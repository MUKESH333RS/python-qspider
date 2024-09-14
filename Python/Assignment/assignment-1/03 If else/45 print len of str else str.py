# 45.	Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is

string = input("Enter a string:")
length = len(string)
if length > 3:
    print(f"The length of the string is {length}")
else:
    print(f"{string}")