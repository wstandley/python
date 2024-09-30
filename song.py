"""
    This is for Assignment PE1 4.2- How functions communicate with their environment
    The song I chose for this assignment is Row, Row, Row Your Boat.
"""

# Define custome song function
def custom_song(vehicle, pathway, emotion, emotion2, noun1, animal, action_verb, exclamation):
    print("\n")
    print(f"Row, row, row your {vehicle},")
    print(f"{emotion} down the {pathway}.")
    print(f"{emotion2} {emotion2} {emotion2} {emotion2}")
    print(f"{noun1} is but a dream.")
    print(f"Row, row, row your {vehicle},")
    print(f"{emotion} down the {pathway}.")
    print(f"if you see an {animal}")
    print(f"don't forget to {action_verb} ({exclamation}!)")

input_vehicle = input("Enter a type of vehicle: ")
input_emotion = input('Enter an emotion ending in "-ly": ')
input_pathway = input("Enter a type of path you can travel on: ")
input_emotion_2 = input('Enter another emotion ending in "-ly": ')
input_noun_1 = input("Enter an object: ")
input_animal = input("Enter an animal: ")
input_action_verb = input("Enter an action verb: ")
input_exclamation = input("Enter an exclamation: ")

custom_song(vehicle = input_vehicle, pathway = input_pathway, emotion = input_emotion, emotion2 = input_emotion_2, noun1 = input_noun_1, animal = input_animal, action_verb = input_action_verb, exclamation = input_exclamation)