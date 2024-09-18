"""
    This is for assignment PE1 3.2A- While Statements in Python
    Writing program to run "99 Bottles of Beer on the Wall"
"""

# Count

count = 99

# While Statement

while count > 2:
    print(f"{count} bottles of beer on the wall\n{count} bottles of beer") # Print Statement

    count = count - 1 # Causes count to subtract one each time

    print(f"Take one down, pass it around\n{count} bottles of beer on the wall!\n")

# While statement at specific count

while count == 2:
    print(f"{count} bottles of beer on the wall\n{count} bottles of beer\nTake one down, pass it around\n{count} bottle of beer on the wall!\n")
    
    count = count - 1
    
while count == 1:
    print(f"{count} bottle of beer on the wall\n{count} bottle of beer\nTake one down, pass it around\nNo bottles of beer on the wall!\n")

    count = count - 1