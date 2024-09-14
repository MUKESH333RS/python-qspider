# 37.	Write a program to check whether a given character is a special symbol or not

char = input("Enter a character:")
if char.isalnum():      # Alternate method - if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
    print(f"A given character {char} is not a special character.")
else:
    print(f"A given character {char} is a special character.")



