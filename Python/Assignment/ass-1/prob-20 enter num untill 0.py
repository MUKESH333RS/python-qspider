# Write a program to enter the number till the user enter ZERO and at th end it should display the count of positive and negative numbers entered.

num = list()
length = 1
while length > 0:
    digit = int(input())
    if digit == 0:
        break
    else:
        num.append(digit)
    length += 1

i = 0
sum1 = 0
length = len(num)
while length > 0:
    sum1 = sum1 + num[i]
    i += 1
    length -= 1

print(sum1)




