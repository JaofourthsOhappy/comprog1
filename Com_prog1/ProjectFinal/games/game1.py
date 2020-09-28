# constant
STAY_VAL = 16
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

import sys
sys.path.insert(1,"others")
from player import *

class Deck : 
    def __init__(self, deck = []):
        """ Initilize deck
        """
        self.deck = deck
    def initialize(self):
        """ Crete deck which has 52 cards
        """
        for rank in RANKS:
            for suit in SUITS:
                card = rank + ' ' + suit
                self.deck += [card]
        return self.deck
    def shuffle(self):
        """ This method can shuffle deck
        """
        import random
        n = len(self.deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.deck[r]
            self.deck[r] = self.deck[i]
            self.deck[i] = temp
        return self.deck

class Hand:
    def __init__(self,hand,value,deck):
        """ Initilize hand
        """
        self.hand = hand
        self.hand_value = value
        self.deck = deck

    def cal_value(self):
        """ This method can calculate hand values
        """
        val = 0
        num_ace =0
        for card in self.hand :
            ltemp = card.split()
            if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                val += int(ltemp[0])
            elif ltemp[0] in ['Jack' , 'Queen' , 'King']:
                val += 10
            else:
                num_ace +=1
        if num_ace == 0 :
            return val
        else :
            if (val + num_ace -1 +11) >21 :
                return val + num_ace
            else:
                return val + num_ace -1 +11

    def draw_card(self,n):
        """ Draw one card from your deck
        """
        for i in range(n):
            self.hand.append(self.deck.pop())
        return self.hand

    def display(self,num =0 ):
        """ display player's hand
        """
        display_str = ""
        for each_card in self.hand:
            ltemp = each_card.split()
            if ltemp[1] == 'Clubs':
                display_str += ltemp[0] + '\u2663' + ' '
            elif ltemp[1] == 'Diamonds':
                display_str += ltemp[0] + '\u2666' + ' '
            elif ltemp[1] == 'Hearts':
                display_str += ltemp[0] + '\u2660' + ' '
            else:
                assert ltemp[1] == 'Spades', 'Spades expected'
                display_str += ltemp[0] + '\u2665' + ' '
        if num == 1 :
            i = len(self.hand[0].split(" ")[0])
            print(display_str[i+1: ])
        else:
            print(display_str)

    def must_draw_more(self):
        """ return True if his hand values is less than 16
        """
        hand_val = self.cal_value()
        if hand_val < STAY_VAL:
            return True
        else:
            return False

    def black_jack(self):
        """  return True  if one player is blackjack
        """
        hand_val = self.cal_value()
        if hand_val == 21 :
            return True
        else:
            return False


class BlackJack: 
    def __init__(self,player):
        """ Initilize for Blackjack
        """
        self.__winner = ""
        self.__game_over = False

        self.player = player
        self.game_id = 1
    # def return_value(self):
        # if self.__winner == "player":
        #     return 1
        # else:
        #     return 0
    def result (self):
        """ Method to update num_play and num_win
        """
        if self.__winner == "player" :
            self.player.update_num_win(self.game_id,1)
        self.player.update_num_play(self.game_id)
        # print(self.player)
    @property    
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self,value):
        self.__winner = value
    @property
    def game_over(self):
        return self.__game_over
    @game_over.setter
    def game_over(self,value):
        self.__game_over = value


    def main(self):
        """ Method to run this game
        """
        print("Let's play blackjack!")
        deck1  = Deck()
        deck1.initialize()
        deck1 = deck1.shuffle()
        #player setting
        player = Hand([],0,deck1)
        player.draw_card(2)
        print("Your hand : " , end = "")
        player.display()
        #computer setting
        computer = Hand([],0,deck1)
        computer.draw_card(2)
        print("Computer hand : " ,end = "")
        computer.display(1)

        player_value = player.cal_value()
        computer_value = computer.cal_value()

        #Check for BlackJack
        if player.black_jack() and computer.black_jack():
            print("Both tie")
        elif computer.black_jack() :
            print("computer win")
        elif player.black_jack():
            print("player win")
        if player.black_jack() or computer.black_jack():
            print("Computer hand : " , end = "")
            computer.display(0)
            #TODO make this program QUIT
        # Check player value
        while player.must_draw_more():
            player.draw_card(1)
            print("Your hand : " , end = "")
            player.display()
            player_value = player.cal_value()
        # Want more card option
        option = input("Want more card ? ")
        while option != 'no' :
            option.lower().startswith("y")
            player.draw_card(1)
            print("Your hand : " , end = "")
            player.display()
            player_value = player.cal_value()
            option = input("Want more card ? ")

        while computer.must_draw_more():
            computer.draw_card(1)
            print("Computer hand : " , end = "")
            computer.display(1)
            computer_value = computer.cal_value()
        if player_value >21 :
            self.__game_over = True
            if computer_value > 21:
                print("Both tie")
            else:
                print("Computer win")
        else:
            self.__game_over = True
            if computer_value >21 :
                print("Player win")
            else :
                while computer_value < player_value :
                    computer.draw_card(1)
                    print("Computer hand : " , end = "")
                    computer.display(1)
                    computer_value = computer.cal_value()             
                if computer_value >21 :
                    print("Player win")
                    self.__winner = "player"
                elif computer_value == player_value :
                    print("Both tie")
                    self.__winner ="none"
                else: 
                    print("Computer win")
                    self.__winner = "computer"
        print("Computer hand Final : " , end = "")
        computer.display(0)
        self.result()
    #     self.update_result()
    # def update_result(self):
    #     if self.__game_over() :
    #         if self.__winner == 'player':
    #             pass

# player = Player("kao",100)
# bj = BlackJack(player)
# bj.main()

