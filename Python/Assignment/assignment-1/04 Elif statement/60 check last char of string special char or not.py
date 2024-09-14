# 60.	Write a program to check whether the last character of a given string is a special character or not.

string = input("Enter a character:")
last_char = string[::-1]
if last_char.isalnum():
    print(f"The last character {last_char} of a given string {string} is not a special character.")
else:
    print(f"The last character {last_char} of a given string {string} is a special character.")