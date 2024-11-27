from Card import Card
import random

class Deck:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    def __init__(self):
        self.deck = [Card(suit, number) for suit in self.suits for number in range(1, 14)]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{[card for card in self.deck]}"
    
    def __shuffleOneCard(self):
        cardToShuffle = self.removeTopCard()
        self.deck.insert(random.randint(0, self.getDeckSize()), cardToShuffle)

    def deckIsEmpty(self):
        return len(self.deck) <= 0
    
    def getDeckSize(self):
        return len(self.deck)

    def addCard(self, card):
        if card in self.deck:
            print("Card is already in deck")
            return
        self.deck.append(card)

    def removeCard(self, card):
        if card not in self.deck:
            print("Card is already removed")
            return
        self.deck.remove(card)

    def removeTopCard(self):
        if self.deckIsEmpty():
            print("Deck is already empty")
            return
        return self.deck.pop(0)

    def shuffleDeck(self):
        for i in range(250):
            self.__shuffleOneCard()
        return self.deck
