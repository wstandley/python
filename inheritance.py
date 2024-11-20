"""
    This is for Assignment PE2 Module 3.5.1.1 OOP Fundamentals: Inheritance

    This Program will take in Employee input with their name, employee number, pay rate, and shift number and display the details
"""

# Set Employee Class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getters and Setters
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    
    def set_name(self, value):
        self.__name = value
    def set_number(self, value):
        self.__number = value

# Set SubClass ProdcutionWorker
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay = pay

    # Getters and Setters
    def get_shift(self):
        return self.__shift
    def get_pay(self):
        return self.__pay
    
    def set_shift(self, value):
        self.__shift = value
    def set_pay(self, value):
        self.__pay = value

    def __str__(self):
        return f"Name: {self.get_name()}\nEmployee Number: {self.get_number()}\nShift: {self.get_shift()}\nPay Rate: {self.get_pay()}"


def main():
    # Main Function
    name = input("Enter Employee Name: ")
    number = int(input("Enter Employee Number: "))
    pay = float(input("Enter Pay Rate: "))
    shift = int(input("Enter Shift Number: "))

    if shift == 1:
        shift = "Day"
    else:
        shift = "Night"

    employee = ProductionWorker(name, number, shift, pay)

    print("\nDetails of Employee: \n\n")
    print(employee)

main()