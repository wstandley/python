"""_summary_
       Demonstration of writing and instantiating a class


"""

# Class definition of a student


class Student:  # class names are capitalized
    # You can/should initialize a class with variables
    def __init__(self, first_name, last_name, student_id, year):
        # declaring the private variables. Starting with __ makes them private
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__year = year

    # method to get student's info as a formattes string
    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, ID: {self.__student_id}, Year: {self.__year}"


def main():
    student_1 = Student("Meri", "Kasprak", "123456", "Super Senior")
    print(student_1.get_info())
    student_2 = Student("Fred", "Flinstsont", "234566", "Freshman")
    print(student_2.get_info())


main()
