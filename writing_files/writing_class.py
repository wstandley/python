
def main():

    # Writing user input to a file
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Open or create the file in write mode
    with open('writing_files/contacts.txt', 'w') as file:  # 'w' mode overwrites existing content
        # Add newline for better formatting
        file.write(name + ', ' + phone + '\n')


main()