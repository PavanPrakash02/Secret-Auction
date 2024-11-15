import os
from art import logo
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print("Welcome to the secret auction program")
auction_bid = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bid[name] = bid
    countinue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if  countinue_bidding.lower() == "yes":
        clear_screen()
        continue
    else:
        break

find_highest_bidder(auction_bid)




