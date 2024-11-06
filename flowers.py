"""
    For Assignment PE2 Module 2.6: Errors
    Creating a program that will ask the user to input names of flowers and add them to a list. Program should be able to handle exceptions
"""

flowers = []

valid = False

def main():
    # Main Function
    valid = True
    print("""Please enter the names off flowers.\nWhen done, type "done"\n\n""")
    while valid != False:
        try:
            # User Input
            user_flowers = input("Input Here: ")
            # Allows the user to say when they are done
            done = 'done'
            # Loop to keep asking flowers until user says done
            if user_flowers != done:
                # Add flower to list
                flowers.append(user_flowers)
            else:
                print("Thank you for the flowers!")
                valid = False
        # Except the ValueError
        except ValueError:
            print("ValueError!")
        # Except the IndexError
        except IndexError:
            print("IndexError!")
        # Except general other errors
        except:
            print("An Error Occured...")
    # Sort the Flowers List
    flowers.sort()
    for flower in flowers:
        # Print the Individual Flowers
        print(flower)



main()