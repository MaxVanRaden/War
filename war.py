#Written by Max Van Raden, 03/11/2022
#CLI implementation of the card game War

# Class to represent playing cards, contains value and name/suit
class card:
    def __init__(self, value: int, name, suit):
        self.value = value # integer value of the card for determining outcomes
        self.name = name 
        self.suit = suit 


def genDeck(deck):

    # Outer loop handles each suit of the deck
    for i in range(4):
        currentSuit = ""
        if i == 0:
            currentSuit = "Diamonds"
        elif i == 1:
            currentSuit = "Hearts"
        elif i == 2: 
            currentSuit = "Spades"
        elif i == 3: 
            currentSuit = "Clubs"
        else:
            raise Exception('Unexpected range value')
        
        # Handles the numerically named cards
        for j in range(9): 
            deck.append(card(j+2, "{}".format(j+2), currentSuit))
        
        # Handles the face cards
        for j in range(4):
            if j == 0:
                deck.append(card(11, "Jack", currentSuit))
            elif j == 1:
                deck.append(card(12, "Queen", currentSuit))
            elif j == 2:
                deck.append(card(13, "King", currentSuit))
            elif j == 3:
                deck.append(card(14, "Ace", currentSuit))
            else: 
                raise Exception('Unexpected range value')

