from Deck import Deck
from Player import Player, Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer("Dealer")
        self.player = Player("Daniel")
    
    def start(self):
        self.dealInitialCards()
        self.player.printHand()
        while self.player.sumOfHand() < 21 and self.player.wantsToKeepPlaying():
            self.askPlayerForHit()
            self.player.printHand()
        if self.player.sumOfHand() == 21:
            print("Blackjack! You win!")
            return
        elif self.player.sumOfHand() > 21:
            print("Bust! You lose!")
            return
        
        self.dealer.printHand()
        while self.dealer.sumOfHand() < 16:
            self.dealer.drawCard(self.deck)
            self.dealer.printHand()
        if self.dealer.sumOfHand() > 21:
            print("Dealer busts! You win!")
            return
        elif self.dealer.sumOfHand() > self.player.sumOfHand():
            print("Dealer wins!")
        elif self.dealer.sumOfHand() == self.player.sumOfHand():
            print("Push!")
        else:
            print("You win!")

    def askPlayerForHit(self):
        doesPlayerWantHit = input("Would you like to hit? (Y/N): ")
        if doesPlayerWantHit in ["Y", "y"]:
            print("hit me")
            self.player.drawCard(self.deck)
        else:
            print("Stand")
            self.player.callsStand()

    def dealInitialCards(self):
        self.deck.shuffleDeck()
        self.player.drawCard(self.deck)
        self.dealer.drawCard(self.deck)
        self.player.drawCard(self.deck)
        self.dealer.drawSecondCard(self.deck)




