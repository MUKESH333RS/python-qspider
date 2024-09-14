# Write a program to find the HCF of two numbers entered from the user.

n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))
if n1 > n2:
    while n2 > 0:
        n1 , n2 = n2 , n1 % n2
    print(n1)
else:
    while n1 > 0:
        n2 , n1 = n1 , n2 % n1
    print(n2)