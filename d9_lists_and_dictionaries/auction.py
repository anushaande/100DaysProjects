import os

print("Welcome to the secret auction program.")
still_bidding = True
bidding = {}

while still_bidding:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidding[name] = int(bid)
    bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if bidders == 'yes':
        still_bidding = True
    else:
        still_bidding = False
    os.system('cls')
max_bid = 0
for bidder in bidding:
    # print(bidding[bidder])
    if bidding[bidder] > max_bid:
        max_bid = bidding[bidder]
        winner = bidder
    
print(f"The winner is {winner} with a bid of {max_bid}")
    

