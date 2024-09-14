# write a program to print table of a number entered from the user.

num_table = int(input("Enter a table of a number:"))
print(num_table,"Tables")
i = 1
while i <= 20:
    print(i,"*",num_table,"=",i * num_table)
    i += 1
