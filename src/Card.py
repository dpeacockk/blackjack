class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        match self.number:
            case 1:
                return f"Ace of {self.suit}"
            case 11:
                return f"Jack of {self.suit}"
            case 12:
                return f"Queen of {self.suit}"
            case 13:
                return f"King of {self.suit}"
            case _:
                return f"{self.number} of {self.suit}"     
                       
    def getNumber(self):
        match self.number:
            case 11 | 12 | 13:
                return 10
            case _: 
                return self.number

    def getSuit(self):
        return self.suit
