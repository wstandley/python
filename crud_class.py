"""
    CRUD- Create, Read, Update, Delete
"""

def menu(customer):
    try:
        print("Greetings! What would you like to do today? ")
        choice = 0
        while choice != 5:
            # Menu will display options, accept a number, then call the appropriate function
            print("1.  Search for and display a record.")
            print("2.  Create a new record.")
            print("3.  Update an existing record")
            print("4.  Delete an existing record")
            print("5.  Quit the program.")
            choice = int(input("Please enter the number of your selection: "))
            if choice == 1:
                display(customer)
            elif choice == 2:
                create(customer)
            elif choice == 3:
                update(customer)
            elif choice == 4:
                delete(customer)
            elif choice == 5:
                print("Goodbye!")
            else:
                print("I don't understand!")
    except Exception as e:
        print("Bad Input...", e)



def check():
    try:
        with open ("data.txt", 'r') as file:
            # using anything else would create a file, we only want to check to see if it exists
            customers = file.readlines()
            return customers
    except FileNotFoundError:
        # Only does if file doesn't exist
        customers = []
        return customers
    except Exception as e:
        print("An Error Occured...", e)

def save(customers):
    # Call anytime a change is made
    # Writes the customer list to the data.txt file
    try:
        with open("data.txt", "w") as file:
            for line in customers:
                file.write(line)
                print(customers)
            print("Successfully saved")
        file.close()
    except Exception as e:
        print("An Error Occured", e)

def create(customers):
    # create a new record, call the save function and save to the external file.
    print("Create a new record!")
    f_name = input("Please enter the first name: ").capitalize()
    l_name = input("Please enrer the last name: ").capitalize()
    email = input("Please enter the email:  ")
    record = f_name + "," + l_name + "," + email + "\n"
    customers.append(record)
    # print(customers)
    save(customers)


# def read(customers):
#     print("Reading...")
# optional approach instead of passing around the list
# Project Creep

def display(customers):
    print("Display")

def find(customers):
    # Find a customer, return the index of the customer
    # search by phone number
    # return index
    # Note: in VERSION 2 - allow searching by last name
    print("Let me look for that record for you.")
    email = input("Please enter the email you want to look for: ")
    my_index = 0
    for line in customers:
        line = line.strip("\n")
        record = line.split(',')
        print(record[2])
        if record[2] == email:
            print("Found!", line)
            return my_index
        else:
            my_index += 1
    print("Record not found for phone: " , email)

def update(customers):
    print("Updating...")
    find(customers)

def delete(customers):
    print("Deleting...")




def main():
    # Menu for the User
    # customer will be the list of customer records
    customer = check() # Does the file exist? If yes, copy to list, if no, create list
    print(customer)
    menu(customer)

    # check()  # does the file exist? create it/ copy to list
    # save()  # save the list to a file
    # create()  # create a new record
    # read()  # read records
    # find()  # find and display a record
    # update()  # change a record
    # delete()  # remove a record
    # display()  # display a record



main()