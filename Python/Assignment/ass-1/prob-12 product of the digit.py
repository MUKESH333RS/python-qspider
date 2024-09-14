# Write a program to find the sum of the digits of the number accepted by user.

num = int(input("Enter a number:"))
if num < 10:
    print(num)
n = num
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print(product)
