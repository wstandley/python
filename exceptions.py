"""
    This is for Assignment PE1 4.7 - Exceptions
"""

# Simple Python program to calculate the square of a number

def square_number():
    # The try statement tries the original input
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
    # The except will trigger if anything other than a whole number is entered
    except ValueError:
        print("You entered an invalid digit.")
    # Reprompts user to enter a whole number
        number = input("Please enter a whole number to square. ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    # Else runs if user inputs whole number first input
    else:
        print(f"The square of {number} is {squared_number}.")
    # Finally always initiates when program is finished
    finally:
        print("\nProgram Successful!")

square_number()

