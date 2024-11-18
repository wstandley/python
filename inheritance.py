"""
    This is for Assignment PE2 Module 3.5.1.1 OOP Fundamentals: Inheritance

    This Program will take in Employee input with their name, employee number, pay rate, and shift number and display the details
"""

# Set Employee Class
class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# Set SubClass ProdcutionWorker
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.shift = shift
        self.pay = pay

    def __str__(self):
        return f"Name: {self.name}\nEmployee Number: {self.number}\nShift: {self.shift}\nPay Rate: {self.pay}"


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