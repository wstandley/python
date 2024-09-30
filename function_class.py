"""
    Class example for functions
    When making functions ALWAYS put a comment
"""
# This is just calling the function
def magic_py():
    # Functions are like magic
    # Call them and something happens
    print("It's Magic!")

magic_py()
 
# This is passing on for the function
def months (years):
   months = 12 * years
   print(f"You are {months} months old!")
 
years = int(input("How many years old are you? "))
months(years)