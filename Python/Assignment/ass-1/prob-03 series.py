# write a while loop statement to print the following series: 10,20,30....300

a = 10
d = 10
while a <= 300:
    if a == 300:
        print(a,end='.')
        break
    print(a, end=',')
    a = a + d
