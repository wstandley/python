"""
    This is for assignment PE2 Module 4.4: The OS Module
    This Assignment will show basic understanding of use 
    of the OS module
"""

import os

def main():
    # Main Function

    # Use os.mkdir() to create new directory named "MyFiles"
    os.mkdir("MyFiles")
    # Inside MyFiles, have Docs, Images, and Videos
    os.mkdir("MyFiles/Docs")
    os.mkdir("MyFiles/Images")
    os.mkdir("MyFiles/Videos")



main()