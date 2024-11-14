# Day 6 (26/10/2023)

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = input("Enter the number of letters for your password:\n")
num_specials = input("Enter the number of special characters:\n")
num_digits = input("Enter the number of numbers:\n")

# Check that all inputs are numbers
if not num_letters.isdigit() or not num_specials.isdigit() or not num_digits.isdigit():
    print("Please enter valid numbers for each category.")
else:
    password_chars = []

    # Adding random letters
    for _ in range(int(num_letters)):
        password_chars.append(random.choice(alphabet))

    # Add random numbers
    for _ in range(int(num_digits)):
        password_chars.append(random.choice(digits))

    # Add random special characters
    for _ in range(int(num_specials)):
        password_chars.append(random.choice(special_chars))

    # Shuffle and display the final password
    random.shuffle(password_chars)
    generated_password = ''.join(password_chars)
    print(f"Your generated password is: {generated_password}")
