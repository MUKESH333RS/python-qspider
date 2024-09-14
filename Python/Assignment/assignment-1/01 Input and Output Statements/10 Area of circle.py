# 10.	Write a Python program to find the area of a circle.
"""
Area of circle formula:
    A = pi * r * r
        r - radius
"""
import math
pi = math.pi
radius = eval(input("Enter a radius:"))

area_of_circle = pi * radius * radius
print(f"The area of Circle is {area_of_circle}")
