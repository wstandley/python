"""
    This is for Assignment PE2 Module 2.7 & 2.8: Handling List Exceptions
"""

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    try:
        # Input for what artist top spot to take
        artist_index = int(input("Enter the spot of the artist to replace: "))
        # Input for what artist to add to list
        artist_name = input("Enter the new artist name: ")


        # Removes Artist from List and replace it
        top_artists[artist_index - 1] = artist_name

        print(f"Updated List: {top_artists}")
        
    # Except those errors
    except (ValueError, IndexError) as e:
        print(f"An error occurred: {e}")
    

main()