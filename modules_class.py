'''
    Class Example for Modules
    Exploring and using python modules
    code credit by chat GPT
    https://chatgpt.com/share/e/6716a770-d5a8-800e-8282-4cac379ab397
'''

# Import the math module
import math as m # m is the alias for math

# Objective: Introduce using modules and the pow() function to calculate power

# Get two numbers from the user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# USe math.pow() to calculate the result
result = m.pow(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is {result}")

"""
    Second Example
"""

import random

print(random.randint(1, 1000))