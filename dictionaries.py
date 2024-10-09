"""
    This is for Assignment PE1 4.6B- Dictionaries
    This program will take in a user input and translate it as the NATO alphabet
    Use txt.upper() to convert input text to upper case ledders to read code
"""

def main():
    # Main will take in input and list each word
    NATO = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliette", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"X-Ray", "Y":"Yankee", "Z":"Zulu"}
    # ^ Dictionary
    
    word = input("Please enter a word: ")
    # Converts all letter to upper case
    word = word.upper()

    for letter in word: # Letter is used to go through each letter in the word input
        print(NATO[letter]) # Prints NATO itteration

main()