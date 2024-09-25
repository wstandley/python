"""
    This is for Assignment PE1 3.4 Lists
"""

# List

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
steps = []
total_steps = 0
average = 0

# User Input

for i in range(len(days)):
    day = days[i]
    steps_taken = int(input(f"How many steps did you take on {day}? "))# Prints input for each day
    steps.append(steps_taken) # Append (Has to be in the for statement line of code)
    total_steps += steps_taken # Only works because of Integer Input
    average += steps_taken
    
# Display of Total Steps Per Day

for i in range(len(steps)):
    step = steps[i]
    print(f"You took {step} steps on {day}. ")

# Display Total Steps for Week
print(f"\nWeek Total Steps: {total_steps}")

# Display Average steps for the week
average = average / steps
print(f"Average Daily Steps: {average}")