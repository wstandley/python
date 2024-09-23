"""
    This is for Assignment PE1 3.4 Lists
"""

# List

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
steps = []

# User Input

for i in range(len(days)):
    day = days[i]
    step = input(f"How many steps did you take on {day}? ")

# Append

steps.append(step)
print(steps)