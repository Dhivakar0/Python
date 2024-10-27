from replit import clear
import art
print(art.logo)
blind_auction = {}
not_finished = True
while not_finished:
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: ₹"))
  blind_auction[name] = bid
  bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if bidder == "yes":
    clear()
  elif bidder == "no":
    not_finished = False
max_bid = 0
max_bidder = ""
for bidder,bid_price in blind_auction.items():
  if bid_price > max_bid:
    max_bid = bid_price
    max_bidder = bidder
print(f"The Winner is {max_bidder} and the bid amount is ₹{max_bid}.")
  

      
    
  
  


