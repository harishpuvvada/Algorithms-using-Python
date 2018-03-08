import random
class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ["Diamonds","Spades","Hearts","Clubs"]:
            for val in range(1,14):
                self.cards.append(Card(suit,val))

    def show(self):
        for card in self.cards:
            print(card.suit,card.value)

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1): #51 to 1 backwards, not 52 cuz automatically last card is shuffled
            r = random.randint(0,i) #picks any number between 0 and i, note: we are starting from 51 and currently at i
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def drawCard(self):
        return self.cards.pop()



class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = [] #cards in player hand

    def draw(self,deck):
        self.hand.append(deck.drawCard())


    def showHand(self):
        for card in self.hand:
            card.show()   #this will call show method of card class

    def discard(self,card):
        self.hand.pop(card)


deck = Deck()
deck.build()
deck.shuffle()

bob = Player("Bob")
bob.draw(deck) #draw only takes card and keeps in hand of player
bob.showHand()
