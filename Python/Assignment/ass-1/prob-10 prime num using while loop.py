# Write a program to check whether a number is prime or not using while loop.

num = int(input("Enter a number to check whether the number is prime or not:"))
if num < 2:
    print("not Prime")
else:
    if num == 2:
        print("prime")
    elif num % 2 == 0:
        print("not Prime")
    else:
        is_prime = True
        i = 3
        while i <= int(num ** 0.5):
            if num % i == 0:
                is_prime = False
                break
            i += 2
        if is_prime:
            print("Prime")
        else:
            print("Not prime")