"""
    This is for Assignment PE1 3.4 Lists
"""

# List

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
steps = []

# User Input

for i in range(len(days)):
    day = days[i]
    steps_taken = input(f"How many steps did you take on {day}? ") # Prints input for each day
    steps.append(steps_taken) # Append (Has to be in the for statement line of code)

# Display of Total Steps

for i in range(len(steps)):
    total_steps = 0 # Variable
    step = steps[i]
    day = days[i]
    print(f"You took {step} steps on {day}. ")