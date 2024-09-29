"""
    This is for Assignment PE1 3.6 Operations on Lists
"""

# Seats Available List
seats_available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Initilized variables
all_full = "seating"

while all_full != "complete":
    for seat in seats_available:
        print(seat)

    all_full = int(input("Please choose what seat you would like\nIf done purchasing enter '0': "))

    if all_full in seats_available:
        seats_available.remove(all_full)
        print("\nYour seat/s are reserved! ")
    elif all_full == 0:
        print("\nYour seat/s are reserved!\nThank you for your purchase! ")
        all_full = "complete"
    else:
        print("\nThis seat is already taken or doesn't exist.\nPlease choose another from the list. ")

    # No more seats avaible
    if len(seats_available) == 0:
        print("\nNo more seats are available!")
        all_full = "complete" # Finished Loop