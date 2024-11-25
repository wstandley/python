"""
    This is for Assignment PE2 Module 4.2: Processing Files
    User will inotu and it will append in seperate txt file
"""

def main():
    # Main Function
    # User Inputs for Date and Time
    date = input("Enter current date: ")
    time = input("Enter current time: ")
    entry = input("Write New Entry: ")

    # Open diary.txt and append
    with open('diary/diary.txt', 'a') as file:
        # a appends users input and stores it in diary.txt
        file.write(date + ', ' + time + '\n' + entry + '\n')
        # writes users inputs into diary.txt file



main()