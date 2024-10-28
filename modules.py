'''
    This is for Assignment PE2 Module 1.1 and 1.2- Modules

    Can't figure out why it wont stop program once correctly guessed
'''

import random # imports the random 
correct = random.randint(1, 100)

def main():
    # Main Function
    try: 
       # User Enters a number to guess
       guess = int(input("Guess a number between 1 and 100: "))
    # Excepts is user doesnt enter a whole number
    except ValueError:
        print("You entered an incorrect digit.")
    # Calculate the Absolute Value of to get the difference range
    difference = abs(guess - correct)
    # if statement to compare how close it is to answer
    if difference == 0:
        print("You guessed it!")
        print("All Done!")
    elif difference <= 5:
        print("Very Hot!")
        main()
    elif difference <= 15:
        print("Hot!")
        main()
    elif difference <= 25:
        print("Cold")
        main()
    else:
        print("Very Cold")
        main()
             
main()