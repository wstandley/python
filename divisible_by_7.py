"""
    Assignment PE1 3.2B- For Loops in Python
    THis program will find all numbers between 1 and 300 that are divisible by 7
"""

for number in range(1, 300): # Set the (start,stop) range
    if number % 7 == 0: # This is to find numbers divisible by 7
        print(number) # If it is divisble by 7 it will print