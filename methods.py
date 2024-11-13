"""
    This is for Assignment PE2 Module 3.4: Object-Oriented Programming- Methods
    This program will have me create a Pet class with attributes: kind, breed, and name
    I will use special mathods and functions to show specific things within the class
"""

class Pet:

    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Get Statements
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    # Set Statements
    def set_kind(self, value):
        self.__kind = value

    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value

    # Print Details of the Pet
    def print_details(self):
        print("Kind of Pet: " + self.__kind)
        print("Breed of Pet: " + self.__breed)
        print("Name of Pet: " + self.__name)


def main():
    # Main Function
    pet_1 = Pet("Dog", "Golden Retriever", "Skippy")
    pet_2 = Pet("Cat", "Orange", "Thomas")
    pet_3 = Pet("Bird", "Parrot", "Squaks")


    # print Details
    pet_1.print_details()
    print("\n")
    pet_2.print_details()
    print("\n")
    pet_3.print_details()
    print("\n")

    # __name__
    print(Pet.__name__) # Prints name of Pet
    # __module__
    print(Pet.__module__) # Prints what moduke Pet is in
    # __bases__
    print(Pet.__bases__) # Prints the base of the class Pet is


main()
