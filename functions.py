"""
    This is for Assignment PE1 4.1- Functions
"""

# Function for square
def sqaure(area):
    area = side * side
    print(f"The area of the square is {area} sqaure units.")
# Funstion for circle
def circle(area):
    area = 3.14 * radius * radius
    print(f"The area of the circle is {area} sqaure units.")

side = int(input("What is the length of one side of the square? "))
radius = int(input("What is the radius of the circle? "))
sqaure(side)
circle(radius)