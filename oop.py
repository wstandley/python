"""
    This is for Assignment PE2 Module 3.2A: A Short Journey from Procedural to Object-Oriented Approaches
"""

# Initialize Class
class Person:
    def __init__(self, name, address, age, phone):
        # Declare Private Variables
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # Get Info as Strings
    def get_info(self):
        return f"\nName: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone Number: {self.__phone} \n"
    
    # Getter for Name
    def get_name(self):
        return self.__name
    
    # Getter for Address
    def get_address(self):
        return self.__address
    
    # Getter for Age
    def get_age(self):
        return self.__age
    
    # Getter for Phone Number
    def get_phone(self):
        return self.__phone
    
    # Setter for Name
    def set_name(self, name):
        self.__name = name

    # Setter for Address
    def set_address(self, address):
        self.__address = address

    # Setter for Age
    def set_age(self, age):
        self.__age = age

    # Setter for Phone Number
    def set_phone(self, phone):
        self.__phone = phone

    
def main():
    # Main Function
    # Myself
    myself = Person("Will Standley", "100 Cool St.", "21", "(888)888-8888")
    # Call get_info function
    print(myself.get_info())

    # First Family Member
    family_member1 = Person("Mark Standley", "200 Cheeseburger St.", "25", "(555)555-5555")
    print(family_member1.get_info())
    
    # Second Family Member
    family_member2 = Person("Catrina Smith", "300 Blackhawk St.", "39", "(000)000-0000")
    print(family_member2.get_info())

main()