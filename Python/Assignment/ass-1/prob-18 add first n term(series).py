# Write a program to add first n terms of the following series using a while loop: 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter a number:"))
n_series = 1
fact = 1
i = 1
while n > 0:
    fact = fact * i
    n_series = n_series + (1 / fact)
    i += 1
    n -= 1

print(n_series)
