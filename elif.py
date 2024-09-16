"""
    This is for assignment PE1 3.1 B: elif
    This code will take in a grade and tell me what letter grade it gets
"""

# Variables
grade = int(input("What numeric grade did you get? "))

# Decisions
if grade < 60:
    print("Your letter grade is: F")
elif grade < 70:
    print("Your letter grade is: D")
elif grade < 80:
    print("Your letter grade is: C")
elif grade < 90:
    print("Your letter grade is: B")
else:
    print("Your letter grade is: A")