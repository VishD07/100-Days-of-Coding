# Building a calculator. 2/11/23
from diagram import cv_logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary of operations, mapping symbols to the functions above
operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    
}

# Main calculator function to handle input, operations, and repeat logic
def calculator():
    print(cv_logo)  # Assuming a logo is defined above; displays the calculator's 'logo'
    
    # Prompt for the first number in the calculation
    num1 = float(input("What is the first number?: "))
    run = True  # Boolean to control loop continuity

    # Loop for performing consecutive calculations if user chooses to
    while run:
        # Display available operations to the user
        for symbol in operations:
            print(symbol)
            
        # Ask the user for an operation
        perform = input("Type a math operation: ")
        
        # Request the next number
        num2 = float(input("What is the next number?: "))
        
        # Retrieve and execute the chosen operation
        calculation = operations[perform]
        answer = calculation(num1, num2)
        
        # Display the result
        print(f"{num1} {perform} {num2} = {answer}")
        
        # Ask if the user wants to continue with the result, start over, or exit
        print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ")

        # Logic to determine next steps based on user input
        if continue_calc == 'y':
            run = True  # Continue using the result for the next operation
            num1 = answer
        elif continue_calc == 'n':
            run = False  # Exit the loop and end the calculator
            print("\nGoodbye.")
        elif continue_calc == 'new':
            calculator()  # Start a fresh instance of the calculator function
        else:
            print("Invalid response.")
            run = False  # Exit on invalid input
            print("\nGoodbye.")

# Start the calculator
calculator()
