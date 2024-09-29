"""
    This is for assignment PE1 3.5: Sorting Simple Lists: Bubble Sort
"""

# list initialization
number = ["first","second","third","fourth","fifth"]
names = []

for i in range(len(number)):
    numbers = number[i]
    name = input(f"What is the {numbers} name? ")
    names.append(name)

# Bubble Sort Time
swapped = True

while swapped:
    swapped = False
    for i in range(len(names)-1): # Goes through each item of the list
        if names[i] > names[i + 1]: 
            swapped = True
            names[i], names [i + 1] = names [i + 1], names[i] # Once they equal it ends the bubble sort

print(names)
names.reverse() # Reverses List
print(names)