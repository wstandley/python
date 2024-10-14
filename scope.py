'''
    This is for Assignment PE1 4.4: Scopes
'''

# Conversion variables are globals
global KILOS
KILOS = 0.453592

global METERS
METERS = 0.0254

def calculate_weight():
    # Function to calculate the users weight into kilos
    weight_lbs = float(input("What is your current weight in pounds? "))
    weight = weight_lbs * KILOS
    return weight

def calculate_height():
    # Function to calculate the users height into meters
    height_in = float(input("What is your current height in inches? "))
    height = height_in * METERS
    return height


# main function
def main():
    bmi = calculate_weight() / (calculate_height() ** 2)
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

main() # Calls main function