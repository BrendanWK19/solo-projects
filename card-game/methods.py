import random

#create a deck of cards
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + "-" + suit)

#randomly deal cards with playerdeck
def deal(phand):
    pcard = deck[random.randint(0,len(deck)-1)]
    #assign values to the drawn card
    if pcard[0] in ['J', 'Q', 'K', '1']: # face cards and 10
        x=10
    elif pcard[0] == 'A': #aces
        if phand <= 10:
            x=11
        elif phand > 10:
            x=1
    else:               #2-9's
        x = int(pcard[0])
    print(pcard)
    deck.remove(pcard)
    return x

