"""
    This is for Assignment PE1 4.6A: Tuples
"""

def main():
    # This Program is for listing out what classes there are to choose from and counting how many there are
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Structures in Python', 'Web Design Fundamentals')
    for classes in programming_classes:
        print(classes)
        length = len(programming_classes)
    print(f"\nThere are {length} classes for programming.")

main()