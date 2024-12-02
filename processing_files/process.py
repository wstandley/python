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
            # Setting total and count to 0 for math 
            total = 0
            count = 0

            lines = file.readlines() # reads line

            for line in lines: 
                line = line.strip('\n') # Takes out newline symbol

                # Prints each line
                print(line)

                number = float(line) # Converts each entry to a float
                total += number # Adds up running total
                count += 1 # Adds up total entries
        

        average = total / count # Calculates Average

        # Print Total
        print(f"Total: {total:.2f}")
        # Print Entry Amount
        print(f"Number of Entries: {count}")
        # Print Average
        print(f"Average: {average:.2f}")
            
    except IOError:
        print("An IOError has occurred. File not found.")



main()