"""
    This is for Assignment PE2 Module 2.7 & 2.8: Handling List Exceptions
"""

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    try:
        # Input for what artist top spot to take
        artist_index = int(input("Enter the index of the artist to replace: "))

        # Input for what artist to add to list
        artist_name = input("Enter the new artist name: ")

        for name in top_artists:
            name = (artist_index - 1)
            # Remove whatever artist is in the index spot
            top_artists.remove(name)
            # Append artist name to the list
            top_artists.append(artist_name)

        print(f"Updated List: {top_artists}")
    except (ValueError, IndexError) as e:
        print(f"An error occurred: {e}")
    

main()