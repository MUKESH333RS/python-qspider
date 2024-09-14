# Write a program to print the fibonacci series till n terms (accept n from user) using while loop.

n = int(input("Enter a number:"))
n1 = 0
n2 = 1
print(n1)
print(n2)
while n-2 > 0:
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
    n -= 1

