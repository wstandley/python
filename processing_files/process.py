"""
    This is for Assignment PE2 Module 4.2: Working with Real Files
    Read through sales_totals.txt and convert each line to a float
    add each number into a running total, and display the total, the count
    and the average
"""

def main():
    # Main Function
    # always in a try statement
    try:
        with open('processing_files/sales_totals.txt', 'r') as file:
            # Opens File
            content = file.readline() # reads line
            content = content.strip('\n') # Takes out newline symbol
            while content:
                print(content, end='  ') # prints each item
                content = file.readline() # readsline
                content = content.strip('\n') # Takes out newline symbol
        for line in content:
            line = float(line) # Converts each entry to a float
            
            # NEED TO ADD LINES TOGETHER
            
            total = line + line
        
        entries = 11
        average = total/entries

        # Print Total
        print(f"Total: {total:.2f}")
        # Print Entry Amount
        print(f"Number of Entries: {entries}")
        # Print Average
        print(f"Average: {average:.2f}")
            
    except IOError:
        print("An IOError has occurred. File not found.")



main()