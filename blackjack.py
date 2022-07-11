
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0   # track of sum
        self.aces = 0    # track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        # Track aces
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        # Basically changing Ace to a 1 or 11 
        # whichsoever is preferable
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet




def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How many chips do you want to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Insufficient chips! You have: {}".format(chips.total))
            else:
                break


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        x = input("Enter 'h' to hit or 's' to stand")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("Player stands. Dealer's Turn")
            playing = False
        
        else:
            print("Sorry, please try again.")
            continue
        
        break




def show_some(player,dealer):
    
    print("\nDEALER'S HAND:")
    print("one card hidden!")
    print(dealer.cards[1])
    
    print("\n")
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):

    print("\nDEALER'S HAND:")
    for card in player.cards:
        print(card)
    print("\n")

    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)



def player_busts(player,dealer,chips):
    print("Player BUSTS!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")









while True:
    
    print('Welcome to BlackJack!')
    print('Get as close to 21 as you can without going over!')
    print('J,Q,K = 10, A = 1 or 11')
    
    deck = Deck()
    deck.shuffle()
          
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    
    player_chips = Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    
    while playing:  # recall this variable from our hit_or_stand function
        
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)
        
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
            

    if player_hand.value <= 21:
          
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        
        show_all(player_hand,dealer_hand)
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
          
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand) 
    
    
    
    print("\nPlayer's total chips =",player_chips.total)
          
    
    new_game = input("Do you want to play another game? (y/n)")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        break





