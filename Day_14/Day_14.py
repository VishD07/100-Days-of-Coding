import random
from di import data
from art import logo, vs

import os      # Required for clearing the console

# Function to clear the console screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def generate_profile():
    rand_idx = random.randint(0, 49)
    person = data[rand_idx]
    name, followers = person['name'], person['follower_count']
    description, location = person['description'], person['country']
    profile_text = f"{name}, a {description}, from {location}."
    return profile_text, followers

def play_game():
    profile_a, followers_a = generate_profile()
    profile_b, followers_b = generate_profile()
    
    # Ensure the profiles are different
    while followers_a == followers_b:
        profile_b, followers_b = generate_profile()
        
    score = 0
    game_continues = True

    while game_continues:
        clear()
        print(logo)
        
        if score > 0:
            print(f"Nice! Current score: {score}")
        
        # Display profiles to compare
        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")

        guess = input("Who has more followers? Type 'a' or 'b': ").lower()
        
        if (guess == 'a' and followers_a >= followers_b) or (guess == 'b' and followers_b >= followers_a):
            score += 1
            if guess == 'a':
                profile_b, followers_b = generate_profile()
            else:
                profile_a, followers_a = generate_profile()
        else:
            print(f"Oops! Final score: {score}")
            game_continues = False
    
    # Ask to play again
    if input("Play again? Type 'y' or 'n': ").lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")

play_game()
