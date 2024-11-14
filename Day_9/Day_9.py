# Buidling silent auction using conepts like dictonary and nesting.  1/11/23

from art import cv_logo
print (cv_logo)

auct_info = []
auct = True

def add_new_bidder(name, bid_amount):
    # Appending new bidder dictionary to auction_info list
    auct_info.append({"name": name, "bid": bid_amount})

def find_highest_bidder(bidders):
    # Finding the highest bid and bidder using max with key
    highest_bidder = max(bidders, key=lambda bidder: bidder['bid'])
    return highest_bidder

while auct:
    print("Welcome to the private bidding auction session")
    name = input("What is your name?: ").title()
    bid = float(input("How much would you like to bid?: $"))
    add_new_bidder(name, bid)

    # Ask if there are more bidders
    others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n").lower()
    if others == 'no':
        auct = False  # End the auction
        winner = find_highest_bidder(auct_info)  # Get highest bidder
        print(f"The highest bidder is {winner['name']} with a ${winner['bid']:.2f}")
        print("Thank you for your participation. But in reallty you didn't get any money sad!!!!")
    else:
        print("\033[H\033[J")  # Clears the screen
