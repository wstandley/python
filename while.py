"""
    This is for assignment PE1 3.2A- While Statements in Python
    Writing program to run "99 Bottles of Beer on the Wall"
"""

# Count

count = 99
while count >= 0:
    print(f"{count} bottles of beer on the wall\n{count} bottles of beer") # Print Statement

    count = count - 1 # Causes count to add one each time

    print(f"Take one down, pass it around {count} bottles of beer on the wall!")
