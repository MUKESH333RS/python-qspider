# 6.	Write a program to find the simple interest.
"""
simple interest formunla
SI = PNR /100
    P - principal amount
    N - no. of years
    R - rate of interest
"""

P = int(input("Enter principal amount:"))
N = int(input("Enter number of years:"))
R = int(input("Enter rate of interest:"))

Simple_interst = (P * N * R) / 100
print(f"The simple interest is {Simple_interst}")
