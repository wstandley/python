'''
    This is for Assignment PE2 Module 1.1 and 1.2- Modules
'''

import random # imports the random 
correct = random.randint(1, 100)

def main():
    # Main Function
    try: # User Enters a number to guess
        guess = int(input("Guess a number between 1 and 100: "))
        abs(guess)
    # Excepts is user doesnt enter a whole number
    except ValueError:
        print("You entered an incorrect digit.")
        main()
    else:
        while guess != correct:
            print("You guess wrong.")
            main()
    finally:
        print("You guess correctly!")

        


main()