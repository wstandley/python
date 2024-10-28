"""
    This is for Assignment PE2 Module 2.2: The nature of strings in Python
"""

def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for letter in example_string:
        print(letter)

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    print(min(example_string))

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string))

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    print(example_string.index("o"))

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    list_of_chars = list(example_string)
    print(list_of_chars)

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    print(example_string.count("o"))

main()
