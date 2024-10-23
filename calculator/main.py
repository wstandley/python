"""
    For Assignment PE2 Module 1.3- Packages
    Demonstrates the use of the calculator package
"""

from math_operations import calculator
def main():
    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)

main()

from math_operations import geometry
def main():
    result = geometry.rectangle(4, 5)
    print(f"Rectangle result: {result}")

    result = geometry.triangle(10, 10)
    print(f"Triangle result: {result}")

    result = geometry.circle(10)
    print(f"Circle result: {result}")

main()