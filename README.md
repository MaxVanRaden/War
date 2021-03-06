# War

## Introduction

This is an implementation of the card game War written in Python. 

As War is a game devoid of player input or choice, there is no user interaction once the the program begins running - it plays itself. However, it does support several command line arguments discussed later. Once the game is complete, the game displays the winner, the number of rounds taken to reach the end, and the total number of cards swapped between players before the game ended. It also displays an estimation of how long the game would have taken had it been played by hand. 

When designing this implementation of War, I based my choices off of the rules as discussed on wikipedia:

[Rules of War](https://en.wikipedia.org/wiki/War_(card_game)#Gameplay)

However, per Wikipedia, some parts of the War ruleset are not agreed upon. Specific rules that I had to make a decision on can be found under 'Game Rules' in the Assumptions section.

## Instructions
1. Download the project.
2. If necessary, install Python.  
3. Run `python -m war` from within the project directory.

This program has no user interaction while running, but accepts several command line arguments.

    Options:    
                 --verbose (-v)     Prints output for each round of combat instead of just the result of the game
                 --slow (-s)        Adds time between each round to make the game's progress observable
                 --help (-h)        Displays the help menu and exits
    
Options can be chained in any order.
Example usage: `python -m war -v -s`
 
## Assumptions

**The following are a list of assumptions that I made during development:**

**General**
 
 - As the goal is to implement the card game war, only the cards in a deck of cards that are relevant to the game of war need to be implemented. Jokers, which are not used in War, will not be implemented. 
 
 - War is an entirely luck-based game. There are no decisions that can be made within the rules of War that allow player choice or strategy to influence the results. Therefore, once the game has begun (ie, once the program has started), user input will not be possible. Control over how the game runs will be provided via command line arguments.

 - War is a two-player card game.
 
 - Because the project goals do not specify the need for any specific type of user interface, I will use a CLI for simplicity. 
  
 - Wikipedia???s description of the rules is complete and accurate, and an implementation of them constitutes a full, accurate implementation of the card game War.
 
 - The first index of the data structure used to represent each deck will be treated as the top card of the deck, and the last index will be treated as the bottom of the deck. i.e., deck[0] will be the top of the deck, and deck[len(deck)-1] will be the bottom of the deck.

 - A round of war played by people takes approximately 10 seconds.

**Game Rules**

 - Wikipedia states that the rules are unclear on what happens when a player runs out of cards during a war, with some sources saying the player loses immediately and others saying the game starts over. I will assume that the former ruling is correct, and treat it as a loss for the player who runs out of cards.

 - Wikipedia states that the rules often do not specify how cards are to be returned to a player???s deck. Therefore, I will assume that when a player wins cards, the order in which the won cards will be inserted into the bottom of the deck is randomized.

## Corner Cases

Because War is a game that does not allow player input, the quantity and risk of corner cases is greatly reduced versus a game or program that has to allow for and handle user inputs.

However, there are still some corner cases to consider. One such case is what happens when a player is not out of cards, but does not have enough cards to participate in a war.
As described under 'Game Rules' in the Assumptions section, this corner case is handled by the player without enough cards to participate in a War instantly losing the game. 

## Further development possibilities 

Were I to redo this project differently, I think the most interesting alternative route would be to revisit the assumptions I made regarding the game rules. As it stands, cards are shuffled whenever they are added to the bottom of a player's deck. However, some versions of the rules allow players to add the cards to the bottom of their deck in an order of their choice.

This seemingly small difference actually changes the game entirely, because it introduces player choice - and therefore strategy - into the game. By counting cards and ordering their cards intentionally, a player can influence the outcome of the game, which introduces two major changes from the version of War that I have implemented. One, it provides a reason to have player interaction with the program, and two, it means that designing a computer-controlled opponent is possible. These would both be interesting challenges to consider and implement, and would make the project substantially more complex. 
