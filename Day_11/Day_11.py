# Blackjack project 3/11/23


from diagrma import cv
import random  # Required for card shuffling

import os      # Required for clearing the console

# Function to clear the console screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def blackjack_game():

    # Function to deal a card from the deck randomly
    def start_deal(cards):
        return random.choice(cards)

    # Determines if the player has lost the game
    def player_loss(player, cpu):
        # Player loses if the CPU has a total of 21 but the player doesn't or if both have 21.
        return (sum(player) != 21 and sum(cpu) == 21) or (sum(player) == 21 and sum(cpu) == 21)

    # Handles the game outcome when player chooses to stop drawing cards
    def done_playing():
        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)
        print(f"Your hand: {player_cards} with a total of {player_sum}.")
        print(f"The computer's hand: {cpu_cards} with a total of {cpu_sum}.")
        
        # Check final conditions for winning, losing, or drawing
        if cpu_sum > 21:
            print("The computer got a bust. You win!")
        elif player_loss(player_cards, cpu_cards):
            print("You lose.")
        elif player_sum == 21 and cpu_sum != 21:
            print("Blackjack! You win!")
        elif player_sum > 21:
            print("Bust! You lose.")
        elif player_sum == cpu_sum:
            print("It's a draw.")
        elif player_sum > cpu_sum:
            print("You win!")
        else:
            print("You lose.")
        
        # Option to play again or exit
        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        if play_again == 'y':
            clear()
            blackjack_game()
        else:
            print("Goodbye.")

    # Handles the continuation of the game when the player chooses to draw more cards
    def keep_playing():
        # Draw a new card for both the player and the computer
        player_cards.append(start_deal(cards))
        cpu_cards.append(start_deal(cards))
        player_sum = sum(player_cards)
        
        # Adjust if Ace causes a bust by switching it from 11 to 1
        if 11 in player_cards and player_sum > 21:
            ace_index = player_cards.index(11)
            player_cards[ace_index] = 1
            player_sum = sum(player_cards)
        
        # Display current hand totals
        print(f"Your hand: {player_cards}, total: {player_sum}")
        print(f"Computer's hand: {cpu_cards}, total: {sum(cpu_cards)}")
        
        # If player's hand exceeds 21, they bust
        if player_sum > 21:
            print("Bust! You lose.")
            play_again = input("Do you want to play again? Type 'y' or 'n': ")
            if play_again == 'y':
                clear()
                blackjack_game()
            else:
                print("Thanks for playing. Goodbye.")
        else:
            # Ask if the player wants to draw again
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                keep_playing()
            else:
                done_playing()
    
    print(cv)  # Assuming logo is defined
    # Initialize the deck and hands
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = [start_deal(cards), start_deal(cards)]
    cpu_cards = [start_deal(cards)]
    
    # Show initial hand and ask player to choose to draw or pass
    print(f"Your cards: {player_cards}")
    print(f"The computer's first card: {cpu_cards}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    
    # Process the player's decision
    if hit == 'y':
        keep_playing()
    else:
        done_playing()

blackjack_game()
