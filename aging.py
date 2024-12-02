"""
    This is for Assignment PE2 Module 4.5: The DATETIME mmodule
    This program will ask the user to input their birth year, month, and date
    It will put it in Year-Month-Date format and than calculate how many
    months, weeks, days, and years they are old
"""

# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

def main():
   
    print("\n\n")
    try:
        today = datetime.today()
        # Gets todays date
        # User Input
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("\nYour birthday is: ")
        # converts integers into strings
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday
        # Takes todays date and subtracts users inputs to calculate days old
        print(f'Difference is {delta.days} days')

        # Takes total days and divides by 365 to get total years old
        delta_years = delta.days // 365.2425
        print(f'You are {delta_years} years old')

        # Calculates total months old
        # Takes total years old and multiplies by 12 months in a year to get total months
        delta_month = delta_years * 12
        # Remaining calculates how many months are missing from delta_month
        remaining = (delta.days - (delta_years * 365) ) // 30
        # Adds the remaining months to toal months
        delta_months = delta_month + remaining

        print(f"You are {delta_months} months old")

        # Calculates total weeks old
        # Takes total days and divides it by 7 to get weeks
        delta_weeks = delta.days / 7
        print(f"You are {delta_weeks:.1f} weeks old")

        print("\n")

      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()