"""
    This is for assignment PE2 Module 3.6: Exceptions Again

    This program will define NotNumericError and will have the user input a number, if they dont it will raise an InvalidInputError
"""

# Set Subclass of Exception class
class NotNumericError(Exception):
    def __init__(self, number, message = "That is not a number"):
        self.number = number
        self.message = message 
        super().__init__(self.message) # Sets super class

    def __str__(self):
        # Prints message when error is caught
        return f"{self.number} -> {self.message}"
    
def isnumeric(number):
    # Raises Error if number is not all numbers
    if not number.isnumeric():
        raise NotNumericError(number) 
        


def main():
    # Main Function
    # User Input
    number = input("Enter a number: ")
    
    try:
        # Runs isnumeric() function
        isnumeric(number)
    # Catches NotNumeric Error
    except NotNumericError as e:
        print(f"Error: {e}")
    else:
        # Only prints if execution runs without error
        print("You Entered a Number!")
    finally:
        print("Game Over")

main()