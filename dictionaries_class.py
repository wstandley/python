'''
    Class Examples for Dictionaries
'''

# create a secret code using dictionaries
def main():
    code = {"A":"🤍", "B":"😃", "C":"😖", "D":"🤣"}

    # Access using keys
    print(code["A"])

    # using get()
    print(code.get("R","😎"))

    # iterate through all keys
    for key in code:
        print(key, code[key])

    # iterate through key value pairs
    for key, value in code.items():
        print(key, value)

main()