"""
    This is for Assignment PE2 Module 2.5: Four Simple Programs
    This program will have the user input a password and than will take that password and validate it with specific criteria
"""

def main():
    valid = False # change to true if all requirements are met

    while not valid:
        valid = True
        print("""PASSWORD REQUIREMENTS: \n 
              Between 8 to 20 characters long.\n 
              Contains at least one uppercase letter.\n 
              Contains at least one lowercase letter.\n 
              Includes at least one number.\n 
              Includes at least one symbol from the set: !@#$%&*.""")

        # User Input to enter password
        password = input("Please enter your password: ")

        # Checks if the password is 8-20 characters
        if 7 < len(password) < 21:
            valid = True
        else:
            valid = False
            print("That is not the right length.\n")

        # Check to see if password has at least one uppercase
        if password.isupper():
            valid = False
            print("You need a lowercase letter.")
        else:
            valid = True
        
        # Check to see if password has at least one lowercase
        if password.islower():
            valid = False
            print("You need an uppercase letter.")
        else:
            valid = True
        
        # Check to see if password has at least one number
        if password.isalpha():
            valid = False
            print("You need one number.")
        else:
            valid = True

    # Check to see if password has at least one letter
        if password.isalnum():
            valid = False
            print("You need at least one letter.")
        else:
            valid = True    

        # Check to see if password has a symbol
        symbols = ['!', '@', '#', '$', '%', '&', '*']
        has_symbols = False
        for s in symbols:
            for c in password:
                if s == c:
                    has_symbols = True
        if has_symbols == False:
            valid = False
            print("You need at least one symbol")

        # If correct password is entered
        if valid:
            try:
                confirm = input("Please confirm password: ")
                if password == confirm:
                    print("Password Successful!")
            except:
                print("An Error Occured...")

main()