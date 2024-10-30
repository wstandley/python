"""
    This is for Assignment PE2 Module 2.4: Strings in Action and List Methods
    This program will take a user inoput where they list 10 books
    The program will then sort the books in a list
"""

# Initializes the list
sorted = []

def main():
    # Main Function
    while len(sorted) < 10:
        # User Input
        book_titles = input("What is a title of a book you have read? ")
        # Titles each book
        book_titles = book_titles.title()
        # Adds book title to sorted list
        sorted.append(book_titles)
        # Sorts list
        sorted.sort()
    
    # For Loop
    for book_titles in sorted:
            print(book_titles)
        
          
main()