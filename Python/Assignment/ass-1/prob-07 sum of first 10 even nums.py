# Write a program to print sum of first 10 Even numbers

num = 10
sum_of_even_nums = 0
i = 0
while num > 0:
    sum_of_even_nums = sum_of_even_nums + i
    i += 2
    num -= 1
print(sum_of_even_nums)