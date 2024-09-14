# 44.	Write a program to check whether the given string is palindrome or not

string = input("Enter a string:")
reverse_string = string[::-1]
if string == reverse_string:
    print(f"The given string {string} is palindrome.")
else:
    print(f"The given string {string} is not a palindrome.")
