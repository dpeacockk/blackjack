class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.playing = True

    def drawCard(self, deck):
        cardDrawn = deck.removeTopCard()
        self.hand.append(cardDrawn)
        self.playerGetsDealt(cardDrawn)

    def sumOfHand(self):
        sum = 0
        sumWithAces = 0
        for card in self.hand:
            if card.getNumber() == 1:
                sumWithAces += 11
            else:
                sumWithAces += card.getNumber()
            sum += card.getNumber()
        if sumWithAces <= 21:
            return sumWithAces
        return sum

    def printHand(self):
        print(f"{self.name} has {self.hand}")

    def playerGetsDealt(self, card):
        print(f"{self.name} gets dealt a {card}")

    def callsStand(self):
        self.playing = False

    def wantsToKeepPlaying(self):
        return self.playing
    
    def resetPlayer(self):
        self.hand = []
        self.playing = True

class Dealer(Player):
    def drawSecondCard(self, deck):
        cardDrawn = deck.removeTopCard()
        self.hand.append(cardDrawn)        
