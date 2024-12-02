"""
    This is for Assignment PE2 Module 4.6: The Calendar Module
    This program will ask the user for their birth month as a number
    then display the calendar for the month of the current year
"""

import calendar
import datetime

def main():
    y = datetime.datetime.now().year
    # Main Function
    try: 
        # User Input for birth month
        birth_month = int(input("What month were you born in (ex: March would be 3)? "))
        # Raise error if input is not a proper months number
        if not 0 < birth_month < 13:
            raise Exception
        
        print(f"\nYour Birth Month Calendar for {y}:\n")
        # Print the Calendarrrrrrr
        print(calendar.month(y , birth_month))


    except Exception as e:
        print("Game Over")




main()