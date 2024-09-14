# 56.	Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.

char = input("Enter a character:")
if char in "aeiouAEIOU":
    list1 = []
    list1.append(char)
    print(list1)
else:
    print(ord(char))

