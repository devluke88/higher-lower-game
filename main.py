import random
from art import logo
from art import vs
from game_data import data
from replit import clear

# Function to generate person from data
def generate_person(data, personA):
    """This function generate person for the game, if the person is exactly the same as personA then will generate a new person."""
    while True:
        person_generated = random.choice(data)
        if person_generated != personA:
            break
    return person_generated

# Function to compare two values and check if user was righ:
def compare_function(user_choice, valueA, valueB):
    """This function compare user answer with value that is generated in compare_value function"""
    def compare_value(valueA, valueB):
        if valueA > valueB:
          return valueA
        else:
          return valueB
    if user_choice == compare_value(valueA, valueB):
        return True
    else:
        return False

# Function to ask user: "Who has more followers?"
def get_user_answer(personA, personB):
    while True:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_answer == 'A':
            user_choice = personA['follower_count']
            return user_choice
        elif user_answer == 'B':
            user_choice = personB['follower_count']
            return user_choice
        else:
            print("None of your answer is 'A' or 'B', please enter it again.")

# Higher-lower game function to start the game
def play_higher_lower(personA, current_score):
    print(logo)
    user_is_right = True
    while user_is_right:
        # Generate person B
        personB = generate_person(data, personA)

        # Print both: person A and person B and 'vs' sign between
        print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}.")
        print(vs)
        print(f"Compare B: {personB['name']}, a {personB['description']}, from {personB['country']}.")

        # Ask: 'Who has more followers?''
        user_choice = get_user_answer(personA, personB)
        
        # Check if user guessed correctly
        user_is_right = compare_function(user_choice, personA['follower_count'], personB['follower_count'])
        if user_is_right:
            current_score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {current_score}")
            personA = personB
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")

current_score = 0
personA = random.choice(data)

play_higher_lower(personA, current_score)