# """
#     Class example for Bubble Sorting
# """

# # Initialize a list of numbers
# numbers = [8, 6, 7, 6, 5, 3, 0, 9]

# # Flag to track if a swap has occurred
# swapped = True

# # Continue looping until no swaps occur
# while swapped:
#     swapped = False  # Reset the flag at the start of each iteration
#     for i in range(len(numbers) - 1):
#         # Compare adjacent elements
#         if numbers[i] > numbers[i + 1]:
#             swapped = True  # A swap is needed
#             # Swap the elements
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

# # Print the sorted list
# print(numbers)



# Initialize a list of names
names = ["Bob", "Carol", "Ted", "Alice", "Anna"]

# Flag to track if a swap has occurred
swapped = True

# make all names lower case

for i in range(0, len(names)):
    names[i] = names[i].lower()

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print(names)