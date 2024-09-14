# Write a program to print sum of first 10 natural numbers

num = 10
sum_of_natural_nums = 0
i = 1
while num > 0:
    sum_of_natural_nums = sum_of_natural_nums + i
    i += 1
    num -= 1
print(sum_of_natural_nums)
