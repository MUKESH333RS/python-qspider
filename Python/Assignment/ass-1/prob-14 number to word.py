# Write a program to display the number name of hte digits of a number entered by user. For example if the number is 231 then output should be Two Three One.

num = int(input("Enter a number:"))
num_to_word = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine"
}
n = str(num)
length = len(n)
i = 0
while i < length:
    digit = n[i]
    print(num_to_word[int(digit)],end=' ')
    i += 1
