"""
    This is for Assignment PE1 4.5: Creating and Organizing Functions (Recursion).
    Creating a program to calculate factorials
"""

def factorial(n):
    if n == 0 or n == 1:
        return print("The factorial is: 1")
    else:
        print(f"The factorial is: {n}")
        return factorial(n - 1)
    
def main():
    n = int(input("Enter in the number you'd like to get the factorial of (non-negative): "))
    fact = factorial(n)
    print(f"The factorial of {n} is: {fact}")

main()

