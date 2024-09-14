# write a while loop statement to print the following series: 105,98,91......7.

a = 105
d =7
while a > 0:
    if a == 7:
        print(a,end='.')
        break
    print(a,end=',')
    a = a - d