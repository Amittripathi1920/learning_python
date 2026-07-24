def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"-----------------------------------------\nThe Winner is {winner.upper()} with a bid of ${highest_bid}.\n-----------------------------------------")




loop = True
bid_data = {}
while loop:
    name = input("What is your name: ")
    bid = int(input("What's your BID? : $"))

    bid_data[name] = bid
    should_continue = input("Are there any other bidders? type [Y/N]: ").lower()

    if should_continue == "y":
        loop = True
    else :
        find_highest_bidder(bid_data)
        loop = False
