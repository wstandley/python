"""
    This is for assignment PE2 Module 3.6: Exceptions Again

    This program will define NotNumericError and will have the user input a number, if they dont it will raise an InvalidInputError
"""

# Set Subclass of Exception class
class NotNumericError(Exception):
    def __init__(self, number, message = "That is not a number"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.number} -> {self.message}"
    
def isnumeric(number):
    # This is Where I'M stuck
    if number :
        raise NotNumericError(number)
    print("Thanks!")
        


def main():
    # Main Function
    number = int(input("Enter a number: "))

    try:
        isnumeric(number)
    except NotNumericError as e:
        print(f"Error: {e}")
    else:
        print("Good Job!")
    finally:
        print("Game Over")

main()