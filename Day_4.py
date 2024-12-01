# day 4 25/10/2023

#rock paper siccor game using random module

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# start of the game

print("Welcome to your death you have to play a roack paper scissor game to stay alive")
options = [rock, paper, scissors] # creating list of our ascii arts so that we can use afterwards
choice = int(input("Now! quickly chose something - Rock - type 0, Paper - type 1 Scissor - type - 2 ")) # telling user to tell number. we took this as integer and put in options 
your_choice = options[choice] # creating variable for our choice number with option list extact so that if we print this we will directly get output of roack paper or scissor
print("You choose") 
print(your_choice) # our choice

comp_choice = random.choice(options)
print("Computer choose")
print(comp_choice)

if your_choice == comp_choice:
    print("Tie")

if your_choice == rock and comp_choice == scissors:
    print("You win")

if your_choice == rock and comp_choice == paper:
    print("Computer wins ")

if your_choice == paper and comp_choice == rock:
    print("You win")

if your_choice == paper and comp_choice == scissors:
    print("Computer wins")

if your_choice == scissors and comp_choice == rock:
    print("Computer wins")

if your_choice == scissors and comp_choice == paper:
    print("You win")

