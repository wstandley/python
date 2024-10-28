"""
    This is for Assignment PE2 Module 2.1: Characters and Strings vs. Computers
    Finding the ASCII values of strings
"""

def main():
    # User Input
    user_input = input("Enter a character: ")

    # In case user puts in more than one character
    while len(user_input) != 1:
        print("Please enter exactly one character. ")
        user_input = input("Enter a character: ")
    
    # Converts to ASCII value
    ascii_value = ord(user_input)

    # Print it!
    print(f"The ASCII value of {user_input} is {ascii_value}")


main()