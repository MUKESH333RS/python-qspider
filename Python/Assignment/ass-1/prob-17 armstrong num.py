# Write a program to check whether a number is armstrong or not.(Armstrong number is a number that is equal to the sum of cubes of its digits : example - 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3

num = int(input("Enter a number:"))
n = num
arm_strong = 0
while n > 0:
    digit = n % 10
    arm_strong = arm_strong + (digit ** 3)
    n = n // 10

if num == arm_strong:
    print("Armstrong")
else:
    print("Not armstrong")