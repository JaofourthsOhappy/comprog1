import pygame
import sys
#? From player import Player
sys.path.insert(1,"games")
sys.path.insert(1,"others")
balance = 100
from game1 import BlackJack
from game2 import *
from game3 import SnakeLadder
from player import Player
from gamestat import Gamestat
from playerhandler import PlayerHandler
from error import *
system = PlayerHandler()

while True:
        define_status = input("Enter your status (admin/player): ")
        if define_status == 'player':
            name =input("Enter your name: ")
            run1 = True
            t_player = Player(name,balance)
            player =system.add_new_player(t_player)
            while run1 :
                print("Select your choice ")
                print("1. Play Blackjack")
                print("2. Play Namtaopoopla")
                print("3. Play Snakeladder")
                print("4. See your Profile")
                print("5. Stop playing")
                option = input()
                if option == '1':
                    # TODO "Player" class method to play 
                    if player.balance <10 :
                        print("You Don't have enought money")
                    else :
                        player.update_balance(-10)
                        bj = BlackJack(player)
                        bj.main()
                elif option == '2':
                    # TODO "Player" class method to play 
                    namtao = Namtao(player)
                    namtao.main()
                elif option == '3':
                    # TODO "Player" class method to play 
                    if player.balance <10 :
                        print("You Don't have enought money")
                    else:
                        player.update_balance(-10)
                        snake_ladder = SnakeLadder(player)
                        snake_ladder.main()
                elif option == '4':
                    # TODO "Player" class method to see profile
                    print(player)
                elif  option == '5':
                    # TODO method to QUIT
                    try:
                        quit_option = input("Back to Main or Quit (M/Q) : ")
                        if quit_option.lower() == 'm':
                            run1 = False
                        elif quit_option.lower() == 'q':
                            sys.exit()
                            system.write_to_file()
                        else:
                            raise ValueError
                    except ValueError:
                        print("Wrong Input!!")
                else:
                    print("Wrong Input!!")
                print()
                
        elif define_status == 'admin' :
            run2 = True
            while run2:
                print("Select your choice")
                print("1. Add new player")
                print("2. Show Players")
                print("3. Add player's balance")
                print("4. Quit")
                choice = input()
                if choice == '1' :
                    # TODO method to add player
                    name =input("Enter your name: ")
                    t_player = Player(name,balance)
                    player =system.add_new_player(t_player)
                elif choice == '2':
                    # TODO method to show players
                    system.show_player()
                elif choice == '3' :
                    # TODO method to add player's balance
                    name = input("Who do you want to add money?")
                    added = float(input("How much money do you want to add?"))
                    system.add_balance(name,added)
                elif choice == '4':
                    # TODO method to QUIT
                    try:
                        quit_option = input("Back to Main or Quit (M/Q) : ")
                        if quit_option.lower() == 'm':
                            run2 = False
                        elif quit_option.lower() == 'q':
                            system.write_to_file()
                            sys.exit()
                        else:
                            raise ValueError
                    except ValueError:
                        print("Wrong Input!!")
                else :
                    print("Wrong Input!!")
        else :
            print("Wrong Input!!")
        