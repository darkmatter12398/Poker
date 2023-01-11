# Name       : Main code for the poker assignment
# Programmer : Rafat Kabir
# Date       : 2022-04-10
# Description: Implements both Hand and Game classes to create a poker game

from standard_deck import *
from poker_class import *

# Instantiates Deck object
deck = Deck()

# Welcomes the user and talks about the scores
print("Welcome to poker, player 1")
print()
print("I shall explain to you the scoring system")
print()
print("High card: 1")
print("Pair: 2")
print("Two pairs: 3")
print("Three of a kind: 4")
print("Straight: 5")
print("Flush: 6")
print("Full house: 7")
print("Four of a kind: 8")
print("Straight flush: 9")
print()

# Asks user if they want to start the game
start_game = input("Start game (y/n)? ")

# Validation for the input of start_game
while (start_game != "y") and (start_game != "n"):
    print()
    print("Error: Please type 'y' or 'n'")
    print()
    
    start_game = input("Start game (y/n)? ")

# If the user answers with "n", then we will close the program
if start_game == "n":
    print()
    print("Understandable. Have a great day!")

# If the user enters "y", then we will continue with the program
while start_game =="y":  
    print()
    print("*Shuffling a deck of cards*")
    
    deck.shuffle() # Shuffles the deck

    # Instantiates hand object for both player 1 and 2
    player_one_hand = Hand()
    player_two_hand = Hand()

    # Ignore this, this is purely for debugging purposes
    #player_one_hand.hand = [Card("1", "Spades", 9), Card("3", "Diamond", 9), Card("4", "Spades", 7), Card("5", "Spades", 7), Card("6", "Spades", 5)]
    #player_two_hand.hand = [Card("1", "Spades", 9), Card("1", "Diamond", 9), Card("1", "Spades", 7), Card("1", "Spades", 7), Card("1", "Spades", 5)]

    #player_one_hand.debugging()
    #player_two_hand.debugging()

    # Instantiates game object with player 1, player 2, and the deck as the parameters
    game = Game(player_one_hand, player_two_hand, deck)
    
    print()
    print("We will now give out the cards to each player")

    # Formulates the hands of each player by giving cards to each player
    game.formulate_hands()

    # Prompts player 1 if they want to change their 0-2 of their cards
    # Changes said cards
    game.changing_hand()

    # Shows the hands of player 1 and 2
    print("*** PLAYER ONE'S HAND ***")
    print(player_one_hand.show_hand())
    print()
    print("Type of hand: " + player_one_hand.identify_hand())
    
    print()
    print("*** PLAYER TWO'S HAND ***")
    print(player_two_hand.show_hand())
    print()
    print("Type of hand: " + player_two_hand.identify_hand())

    # Shows the score of player 1 and 2
    print()
    print("Player 1 score: ", game.show_score_hand_one())
    print("Player 2 score: ", game.show_score_hand_two())

    # Shows the winner of the game
    game.winner()

    # If there is no winner, then we will initiate 1 or 2 rounds of tiebreaking
    game.tie_breaker()

    # Loop back and ask if user wants to play the game again
    print()
    start_game = input("Start game (y/n)? ")

    if start_game == "n":
        print()
        print("Understandable. Have a great day!")
    
    
    

    
    
    

    

    
    
    

    
