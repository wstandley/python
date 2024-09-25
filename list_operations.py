"""
    This is for Assignment PE1 3.6 Operations on Lists
"""

# Seats Available List
seats_available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Initilized variables
all_full = 'seating'

while all_full != 'complete':
    for seat in seats_available:
        print(seat)
        
    all_full = input("Please choose what seat you would like: ")

if all_full in seats_available:
    seats_available.remove(all_full)

# No more seats avaible
if len(seats_available) == 0:
    print("No more seats are available!")
    all_full = 'complete' # Finished Loop