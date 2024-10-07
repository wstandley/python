'''
    Class exmpale for Recursions
'''
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def main():
# # Example usage:
#     num = int(input("Enter a number between 1 and 25. "))
#     print(fibonacci(num))  # Output: 5

# main()

def double_penny(days, amount=0.01):
    """
    Recursive function to calculate the amount of money when a penny is doubled every day.

    days: int - The number of days over which the penny is doubled.
    amount: float - The current amount of money. Default is 0.01, representing 1 penny.
    return: float - The total amount of money after the specified number of days.
    """
    if days == 1:
        return amount
    else:
        print(f"{days}, amount: {amount:.2f}")
        return double_penny(days - 1, amount * 2)

# Example usage
def main():
     days = int(input("Enter the number of days: "))
     total_amount = double_penny(days)
     print(f"Total amount after {days} days: ${total_amount:,.2f}")

main()