'''
Multiple Variable Creation:
    - It is a phenomenon of creating multiple variable in a single line
    Syntax:
        var1,var2,...,varn = val1,val2,...,valn
        Eg:
            x,y,z = 10,20,30
        * Here the number of variable should exactly equal number of values.

            p,q,r = 1,5,p
        * when we are creating multiple variable in single line,
          we should not use variable name as a value,
          which is defining in the same line.
'''

x,y,z = 10,20,30
print(x,y,z)

p,q,r = 1,5,p           # NameError: name 'p' is not defined
print(p)