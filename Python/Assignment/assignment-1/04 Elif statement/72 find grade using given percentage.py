# 72.	Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, grade is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D.

percentage = int(input("Enter your percentage:"))
if percentage > 90:
    print("Grade:'A'")
elif 80 < percentage <= 90:
    print("Grade:'B'")
elif 60 <= percentage <= 80:
    print("Grade:'C'")
else:
    print("Grade:'D'")