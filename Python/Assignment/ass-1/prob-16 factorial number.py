# Write a program to print factorial of a number accepted from user

n = int(input("Enter a number:"))
fact = 1
i = 1
while n > 0:
    fact = fact * i
    i += 1
    n -= 1
print(fact)