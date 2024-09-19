"""
    This is for Assignment PE1 3.3A: Logical Operations
"""

# Input Statements

integer_1 = int(input("Enter a number: "))
integer_2 = int(input("Enter another number: "))

# and statements

# First Example
if integer_1 > 0 and integer_2 > 0:
    print("Both numbers are greater than 0.")
elif integer_1 < 0 and integer_2 < 0:
    print("Both numbers are less than 0.")
elif integer_1 > 0 and integer_2 < 0:
    print(f"{integer_1} is greater than 0, but {integer_2} is not.")
else:
    print(f"{integer_2} is greater than 0, but {integer_1} is not.")

# Second Example
if integer_1 > 50 and integer_2 > 50:
    print("Both numbers are greater than 50.")
elif integer_1 < 50 and integer_2 < 50:
    print("Both numbers are less than 50.")
elif integer_1 > 50 and integer_2 < 50:
    print(f"{integer_1} is greater than 50, but {integer_2} is not.")
else:
    print(f"{integer_2} is greater than 50, but {integer_1} is not.")

# or statements

# First Example
if integer_1 % 5 == 0 or integer_2 % 5 == 0:
    print("Can either number be divisible by 5? Yes")
else:
    print("Can either number be divisible by 5? No")

# Second Example
if integer_1 % 2 == 0 or integer_2 % 2 ==0:
    print("Can either numbers be divisible by 2? Yes")
else:
    print("Can either numbers be divisible by 2? No")

# not statements

# First Example
if not integer_1 > integer_2:
    print(f"{integer_1} is not greater than {integer_2}")
else:
    print(f"{integer_1} is greater than {integer_2}")

# Second Example
if not integer_1 == integer_2:
    print(f"{integer_1} is not equal to {integer_2}")
else:
    print(f"{integer_1} is equal to {integer_2}")