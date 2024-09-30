"""
    Class example for functions
    When making functions ALWAYS put a comment
"""
# # This is just calling the function
# def magic_py():
#     # Functions are like magic
#     # Call them and something happens
#     print("It's Magic!")

# magic_py()
 
# # This is passing on for the function
# def months (years):
#    months = 12 * years
#    print(f"You are {months} months old!")
 
# years = int(input("How many years old are you? "))
# months(years)


# Example 2: Communications
def add_numbers(number1 , number2):
    # number 1 and number 2 are parameters
    return number1 + number2

# Pass in order
total = add_numbers(5, 7)
print(total)

# Override default order
total = add_numbers(number2 = 12, number1 = 7)
print(total)