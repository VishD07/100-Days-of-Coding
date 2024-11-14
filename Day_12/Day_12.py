# number guessing game 6/11/23


from di import y_o
import random

def initialize_game():
    """Initialize the game by choosing difficulty and setting number of guesses."""
    print(y_o)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guess_this = random.randint(1, 100)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    guesses = 10 if difficulty == 'easy' else 5
    
    return guess_this, guesses

def make_guess(guess_this, guesses_left):
    """Prompts the user to make a guess and checks it against the target number."""
    print(f"You have {guesses_left} guess{'es' if guesses_left > 1 else ''} remaining.")
    try:
        attempt = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        return False, guesses_left  # Invalid guess, retry
    
    if attempt > guess_this:
        print("Too high.")
    elif attempt < guess_this:
        print("Too low.")
    else:
        print(f"Correct! The answer was {guess_this}.")
        return True, guesses_left
    
    return False, guesses_left - 1

def guess_the_number():
    while True:
        guess_this, guesses = initialize_game()
        won = False

        while guesses > 0 and not won:
            won, guesses = make_guess(guess_this, guesses)
        
        if not won:
            print("Game over. You've run out of guesses.")
        
        if input("Play again? Type 'y' for yes, any other key to exit: ").strip().lower() != 'y':
            print("Goodbye.")
            break
        print("\n" + "=" * 30 + "\n")

guess_the_number()
