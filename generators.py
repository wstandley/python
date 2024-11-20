"""
    This is for Assignment PE2 Module 4.1: Generators, Iterators, and Closures
    This program will use a generator function with the yield statement in Python 
    to generate all possible two-letter combinations from a given set of characters
"""
# Initialize List
my_list = ['s', 't', 'a', 'n', 'd']

# Define Function to create combinations
def two_letter_combinations():
        # First sift through
        for letter in my_list:
            # Second sift through
            for letters in my_list:
                  '''
                    Both letter and letters each go through my_list therefore when I yield
                    it is able to take letters from each go through and combine them

                    The yield statement below takes both go throughs and combines them and 
                    stores the data for my main function to call it
                  '''
                  yield letter + letters # Add those letters together and store it




def main():
    '''
        combos goes through each combination that was stored from the two_letter_combinations
        function
    '''
    for combos in two_letter_combinations():
          print(combos) # Print the possible combos

main()