"""
    For Assignment PE2 Module 2.6: Errors
    Creating a program that will ask the user to input names of flowers and add them to a list. Program should be able to handle exceptions
"""

# Initializing lists
flowers = []
number = []

valid = False

def main():
    # Main Function
    valid = True
    print("""\nPlease enter the names of flowers.\nWhen done, type "done"\n\n""")
    while valid != False:
        # User Input
        user_flowers = input("Input Here: ")
        # Allows the user to say when they are done
        done = 'done'
        # Loop to keep asking flowers until user says done
        if user_flowers != done:
            # Add flower to list
            flowers.append(user_flowers)
        else:
            print("\nThank you for the flowers!\n")
            valid = False
    # Sort the Flowers List
    flowers.sort()
    for flower in range(len(flowers)):
        # Allows for index number to print for each flower in its spot in the list
        number = flowers[flower]
        # Print the Individual Flowers
        print(f"{flower + 1}. {number}")

    valid = True
    # Gotta get that loop going for bad inputs
    while valid != False:
        try:
            # User input to enter one of the list numbers
            access = int(input("Enter a number for one of the flowers listed above: "))
            # Finds the item in the list while converting users input to index number
            choice = flowers.pop(access - 1)
            # Shows user there choice
            print(f"You chose {choice}")
            # Breaks loop
            valid = False
        # Except the ValueError
        except ValueError:
            print("That's not a number! (ex: 1, 2, 3...)")
            print("Try Again")
        # Except the IndexError
        except IndexError:
            print("Your number was not on the list! ")
            print("Try again")
        # Except general other errors
        except:
            print("Your input didn't work...")
            print("Try Again")
    

main()