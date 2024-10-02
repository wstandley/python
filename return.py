"""
    This is for Assignment PE1 4.3: Returning a Result from a Function
    Writing a Python Function named calculate_interest that computes and returns the simple interest based on given parameters
"""

# Has to be float
principal = float(input("What is the principle amount? "))
rate = float(input("What is the interest rate? "))
time = float(input("How many years is the money going to be borrowed or invested? "))

def calculate_interest(): # Defines the function
    # Simple Interest Formula
    calculated_interest = (principal * rate * time) / 100
    return calculated_interest

calculated_interest = calculate_interest() # Calls the function
print(f"The simple interest for a principal amount of ${principal:,.2f}\nAt an interest rate of {rate}%\nOver a period of {time} years is : ${calculated_interest:,.2f}.")