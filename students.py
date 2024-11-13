"""
    This is for Assignment PE2 Module 3.3: OOP: Properties
    This program should take in the dog owners first and last name
    along with the pets id, name, and typing
"""

# Initialize class
class Dog:

    # Class Variabless
    pet_type = "Dog"
    vet_name = "Standley Veterinarian Offices"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name):
        # Instance Variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name

    # Implement Getter Methods
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    # Implement Setter Methods
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value
    
    # Method to print all details of the pet and owner
    def display_pet_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)



def main():
    # Main Function
    my_dog = Dog("Will", "Standley", "4115", "Sir BarksALot")
    his_dog = Dog("Camren", "Swanson", "3030", "Cheddar Bob")
    her_dog = Dog("Gil", "Harder", "2001", "Grey")

    # Display Info
    my_dog.display_pet_info()
    his_dog.display_pet_info()
    her_dog.display_pet_info()

    # Check if it has a specific attribute
    print(hasattr(my_dog, "_Dog__pet_id")) # True
    print(hasattr(his_dog, "_Dog__pet_name")) # True
    print(hasattr(her_dog, "_Dog__owner_last_name")) # True
    print(hasattr(my_dog, "_Dog__owner_first_name")) # True
    print(hasattr(his_dog, "_Dog__owner_middle_name")) # False


main()