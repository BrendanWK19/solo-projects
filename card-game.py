import random

#create a deck of cards
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]
playerdeck = []
dealerdeck = []
for suit in suits:
    for rank in ranks:
        playerdeck.append(rank + "-" + suit)
        dealerdeck.append(rank + "-" + suit)

#randomly deal cards with playerdeck
phand = 0
def playerdeal():
    pcard = playerdeck[random.randint(0,51)]
    
    #assign values to the drawn card
    if "J" in pcard or "Q" in pcard or "K" in pcard or "10" in pcard: #face cards and 10
        value = 10
        print(value)
    elif "A" in pcard:   #aces
        if phand <= 10:
            value = 11
            print(value)
        elif phand > 10:
            value = 1
            print(value)
    else:               #2-9's
        for i in range(2,10):
            if str(i) in pcard:
                value = i
                print(value)
                break
    print(pcard)
    playerdeck.remove(pcard) #remove card from deck once dealt

#randomly deal cards with dealerdeck
dhand = 0
def dealerdeal():
    dcard = dealerdeck[random.randint(0,51)]
    
    #assign values to the drawn card
    if "J" in dcard or "Q" in dcard or "K" in dcard or "10" in dcard: #face cards and 10
        value = 10
        print(value)
    elif "A" in dcard:   #aces
        if dhand <= 10:
            value = 11
            print(value)
        elif dhand > 10:
            value = 1
            print(value)
    else:               #2-9's
        for i in range(2,10):
            if str(i) in dcard:
                value = i
                print(value)
                break
    print(dcard)
    playerdeck.remove(dcard) #remove card from deck once dealt

playerdeal()
dealerdeal()

#hand
phand = 0
while phand < 22:
    