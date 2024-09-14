# Write a program to reverse the number accepted from the user using while loop.

num = int(input("Enter a number:"))
if num < 10:
    print(num)
n = num
rev = 0
while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n = n // 10

print(rev)