# 57.	Write a program to check whether a given character is uppercase. If it is uppercase, convert it to lowercase.Else PRINT LOWERCASE

char = input("Enter a character:")
if char.isupper():
    print(char.lower())
else:
    print("LOWERCASE")