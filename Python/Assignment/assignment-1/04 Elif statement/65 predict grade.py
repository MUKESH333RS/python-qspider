# 65.	Write a program to predict grade of the student based on the obtained result.

mark = int(input("Enter a mark obtained:"))
if mark > 90:
    print("Grade:'O'")
elif mark > 80:
    print("Grade:'A+'")
elif mark > 70:
    print("Grade:'A'")
elif mark > 60:
    print("Grade:'B+'")
elif mark > 50:
    print("Grade:'B'")
else:
    print("Grade:'U'")