"""
    This is for Assignment PE1 3.7: Lists in Advanced applications | Arrays
"""

# Variables
total = 0

# List Initializations

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

# Input
for time in range(len(time_slots)):
    time = time_slots[time]
    rates = int(input(f"Please enter your heart rate level during the {time} (in nearest whole number): "))
    heart_rates.append([time,rates]) # Allows for input to be added for specific slot
    total += int(rates) # Adds inputs to total variable 

average = round(total/len(heart_rates))
print(f"\nYour average heart rate for today was: {average}")