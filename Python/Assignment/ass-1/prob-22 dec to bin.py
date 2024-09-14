# Write a program to convert Decimal to Binary

dec = int(input("Enter a decimal number(0-9):"))
n = dec
bin = ''
while n > 0:
    bin_digit = n % 2
    bin = str(bin_digit) + bin
    n = n // 2

print(bin)
