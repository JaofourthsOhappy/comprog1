class Error(Exception):
   """Base class for other exceptions"""
   pass
class InvalidInput(Error):
   """Raised when the input is invalid"""
   pass



import sys
sys.path.insert(1,"others")
from player import *


class Board : 
    def __init__(self, name =""):
        """ Initilize a board which has location of snakes and ladders
        """
        self.__current_position = 0
        self.__name  = name
        self.__snakes = {   8: 4,
                                    18: 1,
                                    26: 10,
                                    39: 5,
                                    51: 6,
                                    54: 36,
                                    56: 1,
                                    60: 23,
                                    75: 28,
                                    83: 45,
                                    85: 59,
                                    90: 48,
                                    92: 25,
                                    97: 87,
                                    99: 63
                                }
        self.__ladder = { 3: 20,
                                    6: 14,
                                    11: 28,
                                    15: 34,
                                    17: 74,
                                    22: 37,
                                    38: 59,
                                    49: 67,
                                    57: 76,
                                    61: 78,
                                    73: 86,
                                    81: 98,
                                    88: 91
                                }
        self.__winner = 'None'
        self.__game_over = False
    def moving(self):
        """ Mothod that calculate position after moving and calculate your last position if you ran into an obstacle and return
            your last position 
        """
        current_position =  self.__current_position + self.dice()
        if current_position > 100 : 
            print(f"{self.__name} need {100 - self.__current_position} to go")
            return self.__current_position
        if current_position in self.__snakes :
            print(f"{self.__name} walked to {current_position}")
            print(" ~~~~~~~~>",end = "")
            print(f"{self.__name} got a snake bite.")
            final_position = self.__snakes.get(current_position)
            print(f"{self.__name} is down from {current_position} to {final_position}")
            # print(f"at {final_position}")
            self.set_position(final_position)
        elif current_position in self.__ladder :
            print(f"{self.__name} walked to {current_position}")
            print(f"Lucky!!! {self.__name} found the ladder")
            final_position = self.__ladder.get(current_position)
            print(f"{self.__name} climbed the ladder from {current_position} to {final_position}")
            # print(f"at {final_position}")
            self.set_position(final_position)
        else:
            self.set_position(current_position)            
        return self.get_position()

    def dice(self):
        """ Method use to random number from range 1 to 6 for dice
        """
        import random
        dice_value = random.randint(1,6)
        print(f"{self.__name} got {dice_value}")
        return dice_value

    def get_position (self):
        return self.__current_position
    def set_position(self,value):
        self.__current_position = value

    def set_game_over(self,value):
        self.__game_over = value
    def get_game_over(self):
        return self.__game_over
    def set_winner(self,value):
        self.__winner = value
    def get_winner(self):
        return self.__winner

class  SnakeLadder :
    def __init__(self,player):
        self.player = player
        self.winner= ""
        self.game_id = 3
    def result(self):
        """ Update num_play and num_win of player
        """
        if self.winner == "player":
            self.player.update_num_win(self.game_id,1)
        self.player.update_num_play(self.game_id)
        # print(self.player)
    def main(self):
        """ Method to run this game
        """
        print("Let's play Snakeladder")
        player = Board('you')
        computer = Board('computer')
        turn = 1
        run = True
        while run :
            try :
                option = input("Hit the enter to roll dice : ")
                if option != "":
                    raise InvalidInput
                player_current_pos = player.moving()
                print(f"you're at {player.get_position()}")
                print()
                computer_current_pos = computer.moving()
                print(f"computer's at {computer.get_position()}")
            except InvalidInput :
                print("Invalid Input!!")

            if player.get_position() == 100 or computer.get_position() == 100:
                print("Game over!!! ",end =" ")
                if player.get_position() == 100 :
                    print("You win")
                    self.winner = "player"
                if computer.get_position() == 100:
                    print("Computer win")
                    self.winner = "computer"
                self.result()
                run = False
            turn +=1
            print()
        print(f"You play for {turn}")

