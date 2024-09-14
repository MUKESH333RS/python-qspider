# Write a program to convert binary to decimal.

bin = input("Enter a binary number(0-1):")
length = len(bin)
dec = 0
i = -1
j = 0
while length > 0:
    digit = int(bin[i]) * (2 ** j)
    dec = dec + digit
    j += 1
    i -= 1
    length -= 1

print(dec)

# another method
n = int(bin)
dec = 0
i = 0
while n > 0:
    digit = n % 10
    dec = dec + (digit * 2**i)
    n = n // 10
    i = i + 1

print("The decimal of ",bin,"is",dec)


