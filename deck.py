from random import randrange
class Deck:
    def __init__(self):
        self.cards = ["ace",2,3,4,5,6,7,8,9,10,10,10,10] * 4 * 8
        self.cutoff = randrange(64, 64*3)
    
    def hit(self):
        card = random.choice(self.cards)
        cards.remove(card)
        return card
    def shuffle(self):
        # check if need to shuffle
        if 8*52 - len(self.cards) < self.cutoff:
            self.cards = ["ace",2,3,4,5,6,7,8,9,10,10,10,10] * 4 * 8
            self.cutoff = randrange(64, 64*3)
        return

    
######################
## Strategy for Aces
######################
def ace(total, target):
    if total + 11 > 21:
        return 1
    # if ace gets to my target
    elif total + 11 > target:
        return 11
        
    else:
        return 11
    
######################
## Dealer Aces
######################    
    
def dealer_ace(total, dealer_ace_count):
    if dealer_ace_count == 0 and total+11 < 22
        return 11
    else 
        return 1
    
#######################
### Play Game
#######################

def game(deck, target):
    deck.shuffle()
    
## hands     
    dealer_total = 0
    my_total = 0
    my_cards = []
    dealer_cards = []
    dealer_ace_count = 0
    
    condition = False
    stop_hit = False
    stop_dealer_hit = False
#####################    
#### hit sequence    
####################
    while dealer_total < 22 and my_total < 22 and not condition:
        ### my turn
        if my_total < target:
            new_card = deck.hit()
            if new_card == "ace":
                new_card = ace(my_total, target)
            my_cards.append(new_card)
            my_total = sum(my_cards)
            ## bust
            if my_total > 21:
                return 0
        else:
            stop_hit = True
        ### dealer turn    
        if dealer_total < 17:
            dealer_card = deck.hit()
            if dealer_card == "ace":
                dealer_card = dealer_ace(dealer_total, dealer_ace_count)
                dealer_ace_count += 1
            dealer_cards.append(hit(deck, my_total))
            dealer_total = sum(dealer_cards)
            ### dealer bust
            if dealer_total > 21 
                return 1
        else:
            stop_dealer_hit = True
        if stop_hit and stop_:
            break
#     print("dealer: ", dealer_total)
#     print("Me:", my_total)
    if my_total > 21:
        return 0
    elif dealer_total > 21:
        return 1
    elif my_total > dealer_total:
        return 1
    elif my_total < dealer_total:
        return 0
    else:
        return .5