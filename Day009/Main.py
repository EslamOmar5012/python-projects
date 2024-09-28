from art import gavel
import os

bidders = {}

print(gavel)
print("Wellcome to the secret auction program.")
flag = 1
while True:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bidders[name] = bid
    option = input("Are there any other bidders? Type 'yes' or 'no'.")

    if option == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif option == 'no':
        break
    else:
        print("invalid input")
        flag = 0
        break


def calc_max_bid(dic):
    max_bid = 0
    n = ''
    for bidder in dic:
        if dic[bidder] > max_bid:
            max_bid = dic[bidder]
            n = bidder
    return n


if flag == 1:
    name = calc_max_bid(bidders)
    print(f"Thw winner is {name} with bid ${bidders[name]}!")
