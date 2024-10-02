"""
    This is for Assignment PE1 4.3: Returning a Result from a Function
    Writing a Python Function named calculate_interest that computes and returns the simple interest based on given parameters
"""

def calculate_interest(): # Defines the function
    # Has to be float
    principal = float(input("What is the principle amount? "))
    rate = float(input("What is the interest rate? "))
    time = float(input("How many years is the money going to be borrowed or invested? "))
    # Simple Interest Formula
    total = (principal * rate * time) / 100
    return total

total = calculate_interest() # Calls the function
print(f"The interest accrued will be {total}.")