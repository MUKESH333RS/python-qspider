# Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

n = int(input("Enter the number till you want:"))
number = n
num = list()
while number > 0:
    num.append(int(input()))
    number -= 1

i = 0
sum1 = 0
while i < n:
    sum1 = sum1 + num[i]
    i += 1

print(sum1)