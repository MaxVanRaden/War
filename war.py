# Written by Max Van Raden, 03/11/2022
# CLI implementation of the card game War

# Class to represent playing cards, contains value and name/suit
import math
from random import shuffle


class card:
    
    def __init__(self, value: int, name: str, suit: str):
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
            if j < 0 or j > 8:
                raise Exception('Unexpected range value') 
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

# splits a deck of cards into two equally sized shuffled decks. 
# deck should be of type List[card] with an even number of cards, p1 and p2deck should
# be empty when passed in
def splitDeck(deck, p1Deck, p2Deck):
    
    if len(deck)%2 != 0 and len(deck) != 0:
        raise Exception("Input deck is not even or is empty, deck cannot be equally split")
    if len(p1Deck) != 0 or len(p2Deck) != 0:
        raise Exception("One or both player decks non-empty")
    
    shuffle(deck)
    mid = math.floor(len(deck)/2) # half the length of the starting deck, for splitting
    p1Deck = deck[:mid]
    p2Deck = deck[mid:]
    
    

def playWar():

    deck = [] # initial, full deck of cards
    p1Deck = [] # Player 1's primary deck - if this is empty, player 1 loses
    p2Deck = []
    p1WarDeck = [] # Player 1's war deck - represents cards in play 
    p2WarDeck = []

    genDeck(deck)
    splitDeck(deck, p1Deck, p2Deck)
playWar()