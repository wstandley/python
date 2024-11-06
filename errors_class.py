"""
    Sample using try and except
"""

def main():
    # Main Function
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"10 divided by {number} is: {result}")

    except ZeroDivisionError:
        print("Oops! Can't divide by zero. Try a different number.")
        main()
    except ValueError:
        print("Oh no! That isn't a number!")
        main()
    except:
        print("This isn't a valid input!")
        main()


main()