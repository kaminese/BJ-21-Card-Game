import random

# Issue: Ace card needs to be 1/11
# if the next card is valued at 11(Ace Card) subtract the added values by 10
# if the addedvalues are 11, Ace Card is valued at 1

# DECK OF CARDS and PLAYER HANDS
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value,self.suit)
    
    def total(self):
        if self.value > 10:
            self.value = 10
           # return self.value
        if self.value == 1:
            self.value = 11
           # return self.value
        return self.value
        
    
class DeckofCards:
    def __init__(self):
        self.cards = []
        self.builddeck()

    def builddeck(self):
        for suits in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for values in range(1, 14):
                self.cards.append(Card(suits, values))
    
    # function that reveals the entire deck
    def show(self):
        for cards in self.cards:
            cards.show()
        print('')

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rando = random.randint(0, i)
            self.cards[i], self.cards[rando] = self.cards[rando], self.cards[i]

    def drawacard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def drawcard(self, deck):
        self.hand.append(deck.drawacard())
    
    def showHand(self):
        for card in self.hand:
            card.show() # show each card object

    def addvalues(self):
        addedvalues = 0
        for card in self.hand:
            addedvalues += card.total()
            if addedvalues == 21:
                return "BLACKJACK"
            if addedvalues > 21:
                return "BUST"
        return addedvalues
            
    def gameend(self):
        if self.addvalues() == "BLACKJACK" or self.addvalues() == "BUST":
            return True
        else:
            return False
    
def game(playername):
    # Dealing Stage:
    deck = DeckofCards()
    deck.shuffle()
    deck.show()
    P1 = Player(playername)
    P1.drawcard(deck)
    P1.drawcard(deck)
    P1.showHand()
    print(P1.addvalues())
    
    # Playing Stage
    ask = ''
    while ask != "Stay":
        ask = input("Hit or Stay? ")

        if ask == "Hit":
            P1.drawcard(deck)
            P1.showHand()
            print(P1.addvalues())
            if P1.gameend() == True:
                break
        elif ask == "Stay":
            return P1.addvalues()

# game("Kami")

# TESTING: 
deck = DeckofCards()
deck.shuffle()
deck.show()

Sora = Player("Sora")
Sora.drawcard(deck)
Sora.drawcard(deck)
Sora.drawcard(deck)
Sora.showHand()
