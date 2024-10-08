"""
    This is for Assignment PE1 4.5: Creating and Organizing Functions (Recursion).
    Creating a program to calculate factorials
"""

def factorial(n, num=1):
    # Function to calculate the factorial
    if n == 0 or n == 1:
        return num
    else:
        return factorial(n-1,num * n)
    
def main():
    # Main Function
    n = int(input("Enter in the number you'd like to get the factorial of (non-negative): "))
    fact = factorial(n)
    print(f"The factorial of {n} is: {fact}")

# Calls Function main()
main()