# This is a Class Example for Returning a Result from a function


# EXAMPLE 1

def add_numbers(number1, number2):
    # add two numbers together
    total = number1 + number2
    return total

# Using the function
result = add_numbers(5, 3)
print("The sum is: ", result)


# EXAMPLE 2

# return the divisor and remainder
def division(num1, num2):
    whole = num1//num2
    remainder = num1 % num2
    return whole, remainder

whole, remainder = division(12, 7)
print(f"The answer is {whole} with a remainder of {remainder}.")