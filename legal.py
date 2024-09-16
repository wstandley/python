"""
    This is for assignment PE1 3.1: Making Decisions in Python
"""

# Variables
age = int(input("How old are you? "))

# Decisions
if age < 16:
    print("You are not old enough to drive.")
else:
    print("You are old enough to drive.")
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")
if age < 21:
    print("You are not old enough to buy alcohol.")
else:
    print("You are old enough to purchase alcohol.")
if age < 65:
    print("You are not eligible for a senior discount.")
else:
    print("You are eligible for a senior discount.")