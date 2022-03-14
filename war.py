# Written by Max Van Raden, 03/11/2022
# CLI implementation of the card game War

from math import floor
from random import shuffle
from typing import List, Tuple
from time import sleep
from sys import argv, exit

# Class for representing card information
class Card:
    def __init__(self, value: int, name: str, suit: str):
        self.value = value  # integer value of the card for determining outcomes
        self.name = name
        self.suit = suit


# Generates a standard deck of 52 playing cards
def genDeck(deck: List[Card]) -> List[Card]:

    if len(deck) != 0:
        raise Exception("List argument is not empty")

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

        # Handles the numerically named cards
        for j in range(9):
            deck.append(Card(j + 2, "{}".format(j + 2), currentSuit))

        # Handles the face cards
        for j in range(4):
            if j == 0:
                deck.append(Card(11, "Jack", currentSuit))
            elif j == 1:
                deck.append(Card(12, "Queen", currentSuit))
            elif j == 2:
                deck.append(Card(13, "King", currentSuit))
            elif j == 3:
                deck.append(Card(14, "Ace", currentSuit))
    return deck


# Splits a deck of cards into two equally sized shuffled decks.
def splitDeck(
    deck: List[Card], p1Deck: List[Card], p2Deck: List[Card]
) -> Tuple[List[Card], List[Card]]:

    if len(deck) % 2 != 0 and len(deck) != 0:
        raise Exception(
            "Input deck is not even or is empty, deck cannot be equally split"
        )
    if len(p1Deck) != 0 or len(p2Deck) != 0:
        raise Exception("One or both player decks non-empty")

    shuffle(deck)
    mid = floor(len(deck) / 2)  # half the length of the starting deck, for splitting
    p1Deck = deck[:mid]
    p2Deck = deck[mid:]
    return p1Deck, p2Deck


# Transfers the amount of cards specified by num from the reserve deck to the wardeck,
# returns false if the reserve deck doesn't have enough cards to transfer.
# Also returns the modified decks.
def playCards(
    deck: List[Card], warDeck: List[Card], num: int
) -> Tuple[bool, List[Card], List[Card]]:

    if num < 1:
        raise Exception("Number of cards to remove invalid")
    # check to make sure there's enough cards to draw, if not report failure
    if len(deck) < num:
        return False, deck, warDeck

    # draw cards
    for i in range(num):
        warDeck.insert(
            0, deck.pop(0)
        )  # removes the top card from the reserve deck and adds it to the top of the war deck

    return True, deck, warDeck


# Shuffles and then adds the cards contained in both wardecks to the bottom of the winning player's
# reserve deck. Also empties the wardecks. Returns the number of cards won by the winning player and the modified decks
def getCards(
    deck: List[Card], p1WarDeck: List[Card], p2WarDeck: List[Card]
) -> Tuple[int, List[Card], List[Card], List[Card]]:

    if len(p1WarDeck) < 1 or len(p2WarDeck) < 1:
        raise Exception("One or both wardecks empty")

    tempDeck = p1WarDeck + p2WarDeck  # combine wardecks to shuffle once
    numWon = len(tempDeck)
    shuffle(tempDeck)
    deck = deck + tempDeck  # append wardecks to winning player's reserve deck
    p1WarDeck = []  # set wardecks to empty in preparation for next round
    p2WarDeck = []
    tempDeck = []
    return numWon, deck, p1WarDeck, p2WarDeck


# Simulates the fight between the two players. Returns an int to indicate which player won, or a draw
def battle(p1WarDeck: List[Card], p2WarDeck: List[Card]) -> int:

    if len(p1WarDeck) < 1 or len(p2WarDeck) < 1:
        raise Exception("One or both battling wardecks empty")
    if p1WarDeck[0].value > p2WarDeck[0].value:
        return 1  # return 1, indicating player 1 won the battle
    elif p1WarDeck[0].value < p2WarDeck[0].value:
        return 2  # player 2 won the battle
    else:

        return 0  # the battle was a draw


# Parses command line arguments and modifies the program accordingly
def argHandler(vFlag: bool, sFlag: bool) -> Tuple[bool, bool]:

    if len(argv) == 0:
        return vFlag, sFlag
    else:
        for i in range(1, len(argv)):
            if argv[i] == "-v" or argv[i] == "--verbose":
                vFlag = True
            elif argv[i] == "-s" or argv[i] == "--slow":
                sFlag = True
            elif argv[i] == "-h" or argv[i] == "--help":
                help()
    return vFlag, sFlag


# Displays the help page and exits the program
def help():
    print(
        """
    This program is a command line implementation of the card game War. 
    It has no user interaction while running, but accepts several command line arguments.

    Options:     --verbose (-v)     Prints output for each round of combat instead of just the result of the game 
                 --slow (-s)        Adds time between each round to make the game's progress observable
                 --help (-h)        Displays this menu and exits
    
    Options can be chained in any order.
    Example usage: >>python -m war -v -s
    """
    )
    exit()


# Main gameplay function. Initializes the variables and runs the game
def main():

    # command line argument handling
    vFlag = False
    sFlag = False
    vFlag, sFlag = argHandler(vFlag, sFlag)

    deck = []  # initial, full deck of cards
    p1Deck = []  # Player 1's primary("reserve") deck - if this is empty, player 1 loses
    p2Deck = []
    p1WarDeck = []  # Player 1's war deck - represents cards in play
    p2WarDeck = []
    p1HasCards = True
    p2HasCards = True
    turnCount = 0
    cardCount = 0  # tracks the number of cards that have been swapped between players during the game

    # initialize the decks
    deck = genDeck(deck)
    p1Deck, p2Deck = splitDeck(deck, p1Deck, p2Deck)

    # Main gameplay loop
    while p1HasCards and p2HasCards:
        p1HasCards, p1Deck, p1WarDeck = playCards(p1Deck, p1WarDeck, 1)
        p2HasCards, p2Deck, p2WarDeck = playCards(p2Deck, p2WarDeck, 1)
        victor = 0

        # "War" loop, keeps looping in same round in the event of a draw condition
        while victor == 0 and p1HasCards and p2HasCards:
            victor = battle(p1WarDeck, p2WarDeck)
            if vFlag:
                print(f"Player 1 plays the {p1WarDeck[0].name} of {p1WarDeck[0].suit}!")
                print(f"Player 2 plays the {p2WarDeck[0].name} of {p2WarDeck[0].suit}!")

            if victor == 0:
                p1HasCards, p1Deck, p1WarDeck = playCards(p1Deck, p1WarDeck, 4)
                p2HasCards, p2Deck, p2WarDeck = playCards(p2Deck, p2WarDeck, 4)
                if vFlag:
                    print("The battle is a draw! This means WAR!")
            elif victor == 1:
                numWon, p1Deck, p1WarDeck, p2WarDeck = getCards(
                    p1Deck, p1WarDeck, p2WarDeck
                )
                if vFlag:
                    print(f"Player 1 wins the battle! They win {numWon} cards!\n")
            elif victor == 2:
                numWon, p2Deck, p1WarDeck, p2WarDeck = getCards(
                    p2Deck, p1WarDeck, p2WarDeck
                )

                if vFlag:
                    print(f"Player 2 wins the battle! They win {numWon} cards!\n")
                if sFlag:
                    sleep(1)
            if vFlag:
                print(f"Player 1 has {len(p1Deck)} cards remaining.")
                print(f"Player 2 has {len(p2Deck)} cards remaining.")

            cardCount += numWon
        turnCount += 1

    if p1HasCards == False:
        print("Player 1 is out of cards. Player 2 wins!")
    elif p2HasCards == False:
        print("Player 2 is out of cards. Player 1 wins!")
    else:
        raise Exception("Both players still have cards at end of play function")
    print(
        f"This match took {turnCount} turns to complete, and {cardCount} cards were exchanged."
    )


if __name__ == "__main__":
    main()
