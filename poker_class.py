# Name       : Class file for the poker assignment
# Programmer : Rafat Kabir
# Date       : 2022-04-10
# Description: Contains a Hand class (for the cards inside a hand), and Game class (for the game functions)

from standard_deck import *

# Class for the hand of 5 cards
class Hand():

    # Initalize variables. Mainly arrays that store card objects from the deck
    def __init__(self):
        self.hand = []
        self.hand_value = []
        self.hand_suit = []
        self.hand_rank = []
        self.hand_name = []

        self.pair_values = []

    # Function for adding card attributes onto the various array's from a card
    def add_card(self, card):
        self.hand.append(card)
        self.hand_value.append(card.get_value())
        self.hand_suit.append(card.get_suit())
        self.hand_rank.append(card.get_rank())
        self.hand_name.append(card.get_name())

    # Function for identifying what type of hand it is
    def identify_hand(self):
        sorted_hand = sorted(self.hand_value) # Sorts the array with only values of the cards

        # Variables that determine if there are repeated ranks
        double = 0
        triple = 0
        quadruple = 0
        all_same = False

        start = 0 # The start of the repeated rank array
        end = 0 # The end of the repeated rank array

        pair_slice = [] # The repeated rank array
        
        # For loop to determine if there's repeated ranks
        # Detects if there are repeated values, and if there is, then we will put these repeated values in an array
        # If the length of the array of the repeated values is 2, then we add 1 onto the variable "double" and vice versa
        for i in range(len(self.hand)):
            if i == (len(sorted_hand) - 1):
                pair_slice = sorted_hand[start: end+1]

                if len(pair_slice) == 2:
                    double += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 3:
                    triple += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 4:
                    quadruple += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 5:
                    all_same = True
                    self.pair_values.append(pair_slice)

            # Sees if there the current number is equal to the next number
            # If it is, then add 1 onto "end"
            elif sorted_hand[i] == sorted_hand[i+1]:
                end += 1

            # If not equal, then we will create the repeated rank array
            # We will then see if the length is equal to 2, 3, 4, or 5
            else:
                pair_slice = sorted_hand[start: end+1] # The repeated rank array              

                if len(pair_slice) == 2: # If length is 2, then add onto variable "double"
                    double += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 3:  # If length is 3, then add onto variable "triple"
                    triple += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 4:  # If length is 4, then add onto variable "quadruple"
                    quadruple += 1
                    self.pair_values.append(pair_slice)

                elif len(pair_slice) == 5: #  If length is 5, then all the cards are the same
                    all_same = True
                    self.pair_values.append(pair_slice)

                end += 1
                start = end        

        # If there is 2 repeated cards, along with 3 repeated cards
        # Then it's a full house
        # The rest are self-explanatory
        if (double == 1) and (triple == 1):
            return "Full house"

        elif (double == 2):
            return "Two pairs"

        elif (double == 1):
            return "Pair"

        elif (triple == 1):
            return "Three of a kind"

        elif (quadruple == 1) or (all_same == True):
            return "Four of a kind"

        # If there is no repeated value in the hand
        # Then we will assume that it's one of the other types of hands
        else:
            start = 0
            end = 0

            ctr = 0

            consecutive_ctr = 0

            # Determines if there is repeated suits among the hand
            for i in range(len(self.hand)):
                if i == (len(self.hand_suit) - 1):
                    pass # if it's at the last index, then do nothing
                
                elif self.hand_suit[i] == self.hand_suit[i+1]:
                    ctr += 1

            # Determines if there is consecutive integers among the hand
            for i in range(len(self.hand)):
                    if i == (len(self.hand) - 1):
                        pass
                    
                    elif (self.hand_value[i+1]) == (self.hand_value[i] + 1):
                        consecutive_ctr += 1

            # If all the hands have the same suit
            # The hand will be a "Straight flush" or a "Flush"
            if ctr == 4:
                if consecutive_ctr == 4: # If all the cards are in order, return "Straight flush"
                    return "Straight flush"

                else: # If not, then return "Flush"
                    return "Flush"

            # If the cards are in order
            # But aren't of the same suit
            # Return "Straight"
            elif consecutive_ctr == 4:
                return "Straight"

            else: # If none of the types of hands list, then it has to be a "High card"
                return "High card"

    # Function for purely debugging purposes
    def debugging(self):
        for i in range(len(self.hand)):
            self.hand_value.append(self.hand[i].get_value())
            self.hand_rank.append(self.hand[i].get_rank())
            self.hand_suit.append(self.hand[i].get_suit())
            self.hand_name.append(self.hand[i].get_name())

    # Function for sorting the hand
    def sorted_hand(self):
        sorted_hand = sorted(self.hand_value)
        test_hand = []
        break_out = False
        
        # Loop for creating a duplicate of the "self.hand" array
        for i in self.hand:
            test_hand.append(i)

        j = 0

        self.hand = []
        self.hand_suit = []
        self.hand_rank = [] # Set all hand arrays to sort them from lowest to highest rank
        self.hand_name = []
        self.hand_value = []

        # Loop for sorting hand names by rank
        # Use the duplicated hand array and sorted hand values to append sorted hand names into the "sorted_hand_name" array
        
        for i in range(len(test_hand)):
            break_out = False
            
            while break_out != True:

                # If current value of sorted hand is equal to current value of test hand, then append test hand value to all hand arrays
                if test_hand[j].get_value() == sorted_hand[i]:
                    self.hand.append(test_hand[j])
                    self.hand_suit.append(test_hand[j].get_suit())
                    self.hand_rank.append(test_hand[j].get_rank())
                    self.hand_name.append(test_hand[j].get_name())
                    self.hand_value.append(test_hand[j].get_value())
                    del test_hand[j]
                    
                    break_out = True # Used to break out of loop

                    j = 0

                else:
                    j += 1
        

    # Function for showing the hand
    def show_hand(self):
        string = ""
        num = 0

        # Loop for actually showing the cards in the hand
        for i in range(len(self.hand)):
            num += 1
            
            if i == (len(self.hand) - 1):
                string += str(num) + ") " + self.hand_name[i]

            else:
                string += str(num) + ") " + self.hand_name[i] + "\n"

        return string # Return the variable "string" in the end

    # Function for changing the cards in the hand
    def change_card(self, index, new_card):
        index -= 1 # For acting as an index

        # Loop through the hand array
        for i in range(len(self.hand)):

            # If the index is equal to the current value of i,
            # Delete the object set in the index i in the hand array,
            # Replace it with a new card from the deck
            if index == i:
                del self.hand[i]
                self.hand.insert(i, new_card)

                # For filling the other array with values, suits, etc
                del self.hand_rank[i]
                self.hand_rank.insert(i, new_card.get_rank())

                del self.hand_suit[i]
                self.hand_suit.insert(i, new_card.get_suit())

                del self.hand_value[i]
                self.hand_value.insert(i, new_card.get_value())
                
                del self.hand_name[i]
                self.hand_name.insert(i, new_card.get_name())

    # self.hand getter
    def get_hand(self):
        return self.hand

    # self.hand_value getter
    def get_hand_values(self):
        return self.hand_value

    # self.hand_name getter
    def get_hand_name(self):
        return self.hand_name

# Class for the actual game rules and things beyond the capabilities of the hand class
class Game():

    # Initialize variables
    def __init__(self, hand_1, hand_2, deck):
        self.hand_1 = hand_1 # First player hand object
        self.hand_2 = hand_2 # Second player hand object
        self.score_1 = 0 # Score of first player
        self.score_2 = 0 # Score of second player

        self.deck = deck # Deck object

    # Function for formulating the hands
    def formulate_hands(self):
        print()

        # Loop for alternating between each hand to give a card to each
        for i in range(5):          
            input("Proceed?") # For pausing between each hand
            print()
            
            card = self.deck.get_card() # New card from the deck
            self.hand_1.add_card(card) # Adding the card to the hand

            # Sort the hand after adding the card
            self.hand_1.sorted_hand()
            
            print("Player one's hand:") # Showing the hand afterwards
            print(self.hand_1.show_hand())

            print()
            print(self.deck.show_deck()) 
            input("Proceed?")
            
            print()
            card = self.deck.get_card()
            self.hand_2.add_card(card)

            self.hand_2.sorted_hand()
            
            print("Player two's hand:")
            print(self.hand_2.show_hand())
            print()

            print(self.deck.show_deck())  

    # Function for changing cards in the hand
    def changing_hand(self):
        hand_1_hand_name = self.hand_1.get_hand_name()
        hand_1_hand = self.hand_1.get_hand()

        # Ask player for how many cards they want to change
        num_change = input("How much cards does player 1 want to change: ")
        print()

        # Validation for if they input the wrong number
        while (int(num_change) > 2) or (int(num_change) < 0):
            if num_change > 2:
                print("Error: You can only pick 0-2 cards to change")

            elif num_change < 0:
                print("Error: Please pick a positive number")

            num_change = input("How much cards does player 1 want to change: ")
            print()

        # Loop for how many times they want to change their cards 
        for i in range(int(num_change)):
            string = ""
            num = 0

            print(self.hand_1.show_hand())

            print()
            card_num = input("Which card does player 1 want to change: ") # Input for which card they want to change

            # Validation for if the card number is invalid
            while (int(card_num) > 5) or (int(card_num) < 0):
                if card_num > 5:
                    print("Error: You can only pick between the boundaries of the displayed cards")

                elif card_num < 0:
                    print("Error: Please pick a positive integer")

            # New card from the deck
            card_change = self.deck.get_card()
   
            # Notify the user of which card had been replaced with what
            print()
            print(self.hand_1.get_hand_name()[int(card_num)-1] + " has been replaced with a " + card_change.get_name())
            print()

            # Call the change_card() function to change the designated card
            self.hand_1.change_card(int(card_num), card_change)

            # Sort the hand afterwards
            self.hand_1.sorted_hand()

    # Function for showing the score of the first player
    def show_score_hand_one(self):
        hand_1 = self.hand_1
        hand_2 = self.hand_2

        # Score is based off of the tables (from lowest to highest)
        if hand_1.identify_hand() == "High card":
            self.score_1 = 1

        elif hand_1.identify_hand() == "Pair":
            self.score_1 = 2

        elif hand_1.identify_hand() == "Two pairs":
            self.score_1 = 3

        elif hand_1.identify_hand() == "Three of a kind":
            self.score_1 = 4

        elif hand_1.identify_hand() == "Straight":
            self.score_1 = 5

        elif hand_1.identify_hand() == "Flush":
            self.score_1 = 6

        elif hand_1.identify_hand() == "Full house":
            self.score_1 = 7

        elif hand_1.identify_hand() == "Four of a kind":
            self.score_1 = 8

        elif hand_1.identify_hand() == "Straight flush":
            self.score_1 = 9

        return self.score_1

    # Function for showing the score of the second player
    def show_score_hand_two(self):
        hand_1 = self.hand_1
        hand_2 = self.hand_2

        if hand_2.identify_hand() == "High card":
            self.score_2 = 1

        elif hand_2.identify_hand() == "Pair":
            self.score_2 = 2

        elif hand_2.identify_hand() == "Two pairs":
            self.score_2 = 3

        elif hand_2.identify_hand() == "Three of a kind":
            self.score_2 = 4

        elif hand_2.identify_hand() == "Straight":
            self.score_2 = 5

        elif hand_2.identify_hand() == "Flush":
            self.score_2 = 6

        elif hand_2.identify_hand() == "Full house":
            self.score_2 = 7

        elif hand_2.identify_hand() == "Four of a kind":
            self.score_2 = 8

        elif hand_2.identify_hand() == "Straight flush":
            self.score_2 = 9

        return self.score_2

    # Determines the winner based off of the score
    def winner(self):
        if self.score_1 > self.score_2:
            print()
            print("Player 1 wins!")

        elif self.score_2 > self.score_1:
            print()
            print("Player 2 wins!")

    # Function for determining the tiebreaker
    def tie_breaker(self):

        # Initializing the variables to be used
        hand_1_values = self.hand_1.get_hand_values()
        hand_2_values = self.hand_2.get_hand_values()
        hand_1_hand = self.hand_1.get_hand()
        hand_2_hand = self.hand_2.get_hand()
        
        hand_type = self.hand_1.identify_hand()
        
        sorted_hand_1 = sorted(hand_1_values)
        sorted_hand_2 = sorted(hand_2_values)

        pair_arr_1 = [] # Array with repeated values
        pair_arr_2 = []

        for i in self.hand_1.pair_values: # Recall from the hand class that pair_values is all the repeated values
            for j in i:
                pair_arr_1.append(j)

        for i in self.hand_2.pair_values:
            for j in i:
                pair_arr_2.append(j)

        sorted_pair_arr_1 = sorted(pair_arr_1)
        sorted_pair_arr_2 = sorted(pair_arr_2)
        
        start = 0
        end = 0
        
        no_pair_arr_1 = [] # Array with non-repeated values
        no_pair_arr_2 = []
        
        pair_slice = []

        # Loop to determine the amount of non-repeated values
        for i in range(len(sorted_hand_1)):
            if i == (len(sorted_hand_1) - 1):
                pair_slice = sorted_hand_1[start:end+1]
                
                if len(pair_slice) == 1:
                    no_pair_arr_1.append(pair_slice[0])
            
            elif sorted_hand_1[i] == sorted_hand_1[i+1]:
                end += 1
            
            else:
                end += 1
                
                pair_slice = sorted_hand_1[start:end]

                # If the length of the slice is only 1, then append it to the array
                # Opposite to finding the repeated values
                if len(pair_slice) == 1:
                    no_pair_arr_1.append(pair_slice[0])
    
                start = end

        # Repeat with the other hand
        start = 0
        end = 0
        
        pair_slice = []
        
        for i in range(len(sorted_hand_2)):
            if i == (len(sorted_hand_2) - 1):
                pair_slice = sorted_hand_2[start:end+1]
                
                if len(pair_slice) == 1:
                    no_pair_arr_2.append(pair_slice[0])
            
            elif sorted_hand_2[i] == sorted_hand_2[i+1]:
                end += 1
            
            else:
                end += 1
                
                pair_slice = sorted_hand_2[start:end]
                
                if len(pair_slice) == 1:
                    no_pair_arr_2.append(pair_slice[0])
    
                start = end

        # Sort the non-repeated value arrays to determine the highest value
        no_pair_arr_1 = sorted(no_pair_arr_1)
        no_pair_arr_2 = sorted(no_pair_arr_2)

        # If the scores are the same
        # Initiate tiebreaker
        if self.score_1 == self.score_2:
            print()

            # Input for user-friendly reasons
            input("Tie! A tiebreaker will ensure which player wins.")

            # If it's a high card, a straight, a straight flush, or a flush
            # Determine winner by highest ranked card
            if (hand_type == "High card") or (hand_type == "Straight") or (hand_type == "Straight flush") or (hand_type == "Flush"):
                if sorted_hand_1[-1] > sorted_hand_2[-1]:
                    print()
                    print("Player 1 has the higher ranking card. \n\nPlayer 1 wins!")

                elif sorted_hand_2[-1] > sorted_hand_1[-1]:
                    print()
                    print("Player 2 has the higher ranking card. \n\nPlayer 2 wins!")

                else:
                    print()
                    print("It's still a tie!")

            # If card type is a full house or a two pair
            elif (hand_type == "Full house") or (hand_type == "Two pairs"):
                start = 0
                end = 0

                arr_slice = []

                non_repeated_value_1 = 0
                non_repeated_value_2 = 0

                two_pair_arr_1 = [] # Array for containing only pairs
                two_pair_arr_2 = []

                three_of_a_kind_value_1 = 0 # Variable for the value of the three of a kind
                three_of_a_kind_value_2 = 0

                pair_value_1 = 0 # Value for the pair
                pair_value_2 = 0

                # Loop for determining the three of a kind and the pair
                for i in range(len(hand_1_hand)):
                    if i == (len(hand_1_hand) - 1):                     
                        arr_slice = sorted_hand_1[start:end+1]

                        if len(arr_slice) == 3:
                            three_of_a_kind_value_1 = arr_slice[0]

                        elif len(arr_slice) == 2:
                            pair_value_1 = arr_slice[0]
                            two_pair_arr_1.append(arr_slice)

                        elif len(arr_slice) == 1:
                            non_repeated_value_1 = arr_slice[0]
                    
                    elif sorted_hand_1[i] == sorted_hand_1[i+1]:
                        end += 1

                    else:
                        end += 1
                        
                        arr_slice = sorted_hand_1[start:end]

                        if len(arr_slice) == 3: # If the length of the slice is 3, then it's a three of a kind
                            three_of_a_kind_value_1 = arr_slice[0]
                        
                        elif len(arr_slice) == 2: # If the length of the slice is 2, then it's a pair
                            pair_value_1 = arr_slice[0]
                            two_pair_arr_1.append(arr_slice)

                        elif len(arr_slice) == 1:
                            non_repeated_value_1 = arr_slice[0]

                        start = end

                start = 0
                end = 0

                # For the second player
                for i in range(len(self.hand_2.hand)):
                    if i == (len(self.hand_2.hand) - 1):
                        arr_slice = sorted_hand_2[start:end+1]

                        if len(arr_slice) == 3:
                            three_of_a_kind_value_2 = arr_slice[0]
                        
                        elif len(arr_slice) == 2:
                            pair_value_2 = arr_slice[0]
                            two_pair_arr_2.append(arr_slice)

                        elif len(arr_slice) == 1:
                            non_repeated_value_2 = arr_slice[0]
                    
                    elif sorted_hand_2[i] == sorted_hand_2[i+1]:
                        end += 1

                    else:
                        end += 1

                        arr_slice = sorted_hand_2[start:end]

                        if len(arr_slice) == 3:
                            three_of_a_kind_value_2 = arr_slice[0]

                        
                        elif len(arr_slice) == 2:
                            pair_value_2 = arr_slice[0]
                            two_pair_arr_2.append(arr_slice)

                        elif len(arr_slice) == 1:
                            non_repeated_value_2 = arr_slice[0]

                        start = end

                # Tie breaker for the two pairs hand type
                if (hand_type == "Two pairs"):
                    all_pairs_values_1 = []
                    all_pairs_values_2 = []

                    highest_pair_value_1 = 0
                    highest_pair_value_2 = 0
                    
                    for i in two_pair_arr_1:
                        for j in i:
                            all_pairs_values_1.append(j)

                    for i in two_pair_arr_2:
                        for j in i:
                            all_pairs_values_2.append(j)

                    all_pairs_values_1 = sorted(all_pairs_values_1)
                    all_pairs_values_2 = sorted(all_pairs_values_2)

                    highest_pair_value_1 = all_pairs_values_1[-1]
                    highest_pair_value_2 = all_pairs_values_2[-1]

                    # Check for highest pair value
                    if highest_pair_value_1 > highest_pair_value_2:
                        print()
                        print("Player 1 has the higher ranking pair")
                        print("Player 1 wins!")

                    elif highest_pair_value_2 > highest_pair_value_1:
                        print()
                        print("Player 2 has the higher ranking pair")
                        print("Player 2 wins!")

                    # If they are the same, then check for individual pairs
                    else:
                        print()
                        input("Since it's still a tie, we'll be looking at individual pairs")
                        
                        if two_pair_arr_1[0][0] > two_pair_arr_2[0][0]:
                            print()
                            print("Player 1 has the higher ranking pair")
                            print("Player 1 wins!")
                            
                        elif two_pair_arr_2[0][0] > two_pair_arr_1[0][0]:
                            print()
                            print("Player 2 has the higher ranking pair")
                            print("Player 2 wins!")

                        else:
                            print()
                            input("Since it's still a tie, we'll be looking at the next pair")
                            
                            if two_pair_arr_1[1][0] > two_pair_arr_2[1][0]:
                                print()
                                print("Player 1 has the next higher ranking pair")
                                print("Player 1 wins!")

                            elif two_pair_arr_2[1][0] > two_pair_arr_1[1][0]:
                                print()
                                print("Player 2 has the next higher ranking pair")
                                print("Player 2 wins!")

                            else:
                                print()
                                input("Since it's still a tie, we'll be looking at the non-repeated ranked card")
                                
                                if non_repeated_value_1 > non_repeated_value_2:
                                    print()
                                    print("Player 1 has the higher ranking non-repeated_card")
                                    print("Player 1 wins!")
                                    
                                elif non_repeated_value_2 > non_repeated_value_1:
                                    print()
                                    print("Player 2 has the higher ranking non-repeated_card")
                                    print("Player 2 wins!")

                                else:
                                    print()
                                    print("It's STILL a tie!")

                # Tie breaker for the full house hand type
                else:
                        
                    # Winner determined by whichever three of a kind value is greater
                    if three_of_a_kind_value_1 > three_of_a_kind_value_2:
                        print()
                        print("Player 1 has the higher ranked three pair.")
                        print("Player 1 wins!")

                    elif three_of_a_kind_value_2 > three_of_a_kind_value_1:
                        print()
                        print("Player 2 has the higher ranked three pair.")
                        print("Player 2 wins!")

                    else:
                        print()
                        input("Since it's still a tie, we'll be looking at the highest pair value")

                        # If their both the same, then winner is determined by the highest pair value
                        if pair_value_1 > pair_value_2:
                            print()
                            print("Player 1 has the higher ranking pair")
                            print("Player 1 wins!")

                        elif pair_value_2 > pair_value_1:
                            print()
                            print("Player 2 has the higher ranking pair")
                            print("Player 2 wins!")

                        else:
                            print()
                            print("It's STILL a tie!")

            # If the hand is any other hand type (hands that have repeated values, apart from full house)   
            else:
                # Score determined by which hand has the higher repeated value
                if sorted_pair_arr_1[-1] > sorted_pair_arr_2[-1]:
                    print()
                    print("Player 1 has the higher ranking " + self.hand_1.identify_hand() + ".")
                    print("Player 1 wins!")

                elif sorted_pair_arr_2[-1] > sorted_pair_arr_1[-1]:
                    print()
                    print("Player 2 has the higher ranking " + self.hand_1.identify_hand() + ".")
                    print("Player 2 wins!")

                # This is a special case.
                # If the hands are the exact same by rank, then we'll just assume it's a tie
                elif sorted_hand_1 == sorted_hand_2:
                    print()
                    print("It's still a tie!")

                # If the repeated values are still the exact same
                # Then determine winner by the highest ranked card (excluding repeated values)
                else:
                    print()
                    input("Since it's still a tie, we'll be determining the winner from the highest ranked card")
                    
                    if no_pair_arr_1[-1] > no_pair_arr_2[-1]:
                        print()
                        print("Player 1 has the higher ranking card")
                        print("Player 1 wins!")
                    
                    elif no_pair_arr_2[-1] > no_pair_arr_1[-1]:
                        print()
                        print("PLayer 2 has the higher ranking card")
                        print("PLayer 2 wins!")
                    
                    else:
                        print()
                        print("It's STILL a tie!")
