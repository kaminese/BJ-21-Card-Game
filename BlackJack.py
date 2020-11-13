import random

# DECK OF CARDS and PLAYER HANDS
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value,self.suit)
    
    def total(self):
        #
        if self.value > 10:
            self.value = 10
            return self.value
        if self.value == 1:
            self.value = 11
            return self.value
        else:
            return self.value
    
class DeckofCards:
    def __init__(self):
        self.cards = []
        self.builddeck()

    def builddeck(self):
        for suits in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for values in range(1, 14):
                self.cards.append(Card(suits, values))
    
    def show(self):
        for cards in self.cards:
            cards.show()

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
        addedvalues = 0
        for card in self.hand:
            card.show()
            addedvalues += card.total()
            if addedvalues == 21:
                return "BLACKJACK"
            if addedvalues > 21: 
                return "BUST"
        print(addedvalues)

deck = DeckofCards()
deck.shuffle()
# deck.show()

# R1:
Dealer = Player("Dealer")
Kami = Player("Kami")

Dealer.drawcard(deck)
Kami.drawcard(deck)
Dealer.drawcard(deck)
Kami.drawcard(deck)

Kami.showHand()
Dealer.showHand()





