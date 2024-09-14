# Q9. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

start = int(input("Enter a starting number:"))
end = int(input("Enter a ending number:"))
if start % 2 == 0:
    current = start
else:
    current = start + 1
while current <= end:
    print(current,end=' ')
    current += 2



