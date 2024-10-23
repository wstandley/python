"""
    This is for Assignment PE2 Module 1.3- Packages
    This program is for calculating the area of a rectangle, triangle, and cricle
"""

def rectangle(length, width):
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = length * width
    print(f"The area of the ractangle is: {area}")
    return area

def triangle(base, height):
    base = float(input("What is the base of the triangle? "))
    height = float(input("What is the height of the triangle? "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
    return area

def circle(radius):
    radius = float(input("What is the radius of the circle? "))
    area = 3.14 * (radius ** 2)
    print(f"The area of the circle is: {area}")
    return area
