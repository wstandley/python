'''
    This is for Assignment PE1 4.4: Scopes
'''

# Conversion variables are globals
global KILOS
KILOS = 0.453592

global METERS
METERS = 0.0254

# main function
def main():
    # user input
    weight_lbs = float(input("What is your current weight in pounds? "))
    height_in = float(input("What is your current height in inches? "))
    # calculations based off input
    weight = weight_lbs * KILOS
    height = height_in * METERS
    bmi = weight / (height * height)
    # function works
    return bmi

bmi = main() # Makes bmi the variable for output of main function

# Print Statements
print(f"Your BMI is: {bmi:.2f}")

# Takes bmi and prints statement depending on outcome from main function
if bmi < 18.5:
    print("You are in the underweight caategory.")
elif bmi < 24.9:
    print("You are in the normal weight category.")
elif bmi < 29.9:
    print("You are in the overweight category.")
else:
    print("You are in the obese category.")