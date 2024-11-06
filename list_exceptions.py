"""
    This is for Assignment PE2 Module 2.7 & 2.8: Handling List Exceptions
"""

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    try:
        artist_name = int(input("Enter the index of the artist to replace: "))
    except (ValueError, IndexError) as e:
        print(f"An error occurred: {e}")
    

main()