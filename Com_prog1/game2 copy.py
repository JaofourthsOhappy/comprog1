
SQUARESIZE = 150
NUM_ROWS = 3
NUM_COLS = 6

WIDTH = NUM_COLS * SQUARESIZE   # 900
HEIGHT = NUM_ROWS * SQUARESIZE #900
import pygame
import sys
import os
sys.path.insert(1,"others")
from player import *

namtao = pygame.image.load(os.path.join("images/namtao.png"))
crab = pygame.image.load(os.path.join("images/crab.png"))
fish = pygame.image.load(os.path.join("images/fish.png"))
tiger = pygame.image.load(os.path.join("images/tiger.png"))
chick = pygame.image.load(os.path.join("images/chick.png"))
shrimp = pygame.image.load(os.path.join("images/shrimp.png"))
play_botton = pygame.image.load(os.path.join("images/play.png"))
tick= pygame.image.load(os.path.join("images/tick.png"))
yes = pygame.image.load(os.path.join("images/yes.png"))
no = pygame.image.load(os.path.join("images/no.png"))

CHOICE = ['namtao','crab','fish','tiger','chick','shrimp']

class Board :
    def __init__(self,life_point):
        self.__grid_lines = [ ((0,0) , (0,900)),
                                         ((0,0) , (900,0)) ,
                                         ((0,150) , (900,150)) ,
                                         ((0,300) , (900,300)) ,
                                         ((0,450) , (900,450)) ,
                                         ((900,0) , (900,900)),
                                         ((150,150) ,(150,900)) ,
                                         ((300,150) ,(300,900)) ,
                                         ((450,150) ,(450,900)) ,
                                         ((600,150) ,(600,900)) ,                                         
                                         ((750,150) , (750,900))]
        self.__grid = [[0 for x in range(6)] for y in range(3)]
        self.__game_over = False
        self.__place_bet =  True
        self.__live_points = life_point

    def draw(self,screen,choose):
        for line in self.__grid_lines :
            pygame.draw.line(screen , (255,255,255) , line[0], line[1] ,3)
        screen.blit(namtao , (0 , 150 ))
        screen.blit(crab , (150,150))
        screen.blit(fish , (300,150))
        screen.blit(tiger , (450,150))
        screen.blit(chick , (600,150))
        screen.blit(shrimp, (750,150))
        screen.blit(play_botton , (750,0))
        for y in range (len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.get_cell_value(x,y) == 'X':
                    screen.blit(tick , (x*SQUARESIZE,y *SQUARESIZE))
        font = pygame.font.SysFont("comicsans" , 58 ,True)
        life = font.render(f"Your life is {self.__live_points}" , 1 , (255,255,255))
        screen.blit(life,(450,20))
        if self.__game_over:
            font = pygame.font.SysFont("comicsans" , 48 ,True)
            play_again = font.render("Do you want to play again ?" , 1 , (255,255,255))
            dealer_choose = font.render(f"Choose {CHOICE[choose[0]]} {CHOICE[choose[1]]} {CHOICE[choose[2]]}" , 1, (255,255,255))
            screen.fill((0,0,0))         
            font = pygame.font.SysFont("comicsans" , 58 ,True)
            life = font.render(f"Your life is {self.__live_points}" , 1 , (255,255,255))
            screen.blit(life,(150,180))
            screen.blit(play_again , (150,250))
            screen.blit(dealer_choose , (150,100))
            screen.blit(tick , (250,300))
            screen.blit(no,(500,300))


    def print_grid(self):
        print(self.__grid[2])

    def get_mouse(self, x, y , choose,screen):
        if self.__place_bet :
            if self.get_cell_value(x,y) == 0 and y == 2:
                self.set_cell_value(x,y,"X")
            else :
                self.set_cell_value(x,y,0)
                screen.fill((0,0,0))
        if self.OK(x,y) and self.count_place() > 0 :
            self.__place_bet = False
            self.check_grid(x,y,choose)

    def check_grid(self,x,y,choose):
        for i in range(len(self.__grid[2])):
                if self.__grid[2][i] == 'X':
                    self.__game_over = True
        count_win = 0
        count_lose=0
        player_choose_list =[]
        for i in range(len(self.__grid[2])):
            if self.__grid[2][i] == 'X':
                player_choose_list.append(i)
        for j in range(len(choose)):
            if choose[j] in player_choose_list :
                count_win +=1
        for k in player_choose_list:
            if k not in choose :
                count_lose +=1
        for i in range(count_win):
            self.winning()
        for j in range(count_lose):
            self.losing()

    def check_die(self):
        if self.__live_points <= 0 :
            return True
        else:
            return False
    def end_game(self):
        if not self.check_die():
            return False
        else: 
            return True
    @property
    def life_point(self):
        return (self.__live_points)
    @life_point.setter
    def life_point(self,value):
        self.__live_points = value
    def get_place_bet(self):
        return self.__place_bet
    def set_place_bet(self,value):
        self.__place_bet = value
    def get_game_over(self):
        return self.__game_over
    def set_game_over(self,value):
        self.__game_over = value
    def get_cell_value(self,x,y):
        return self.__grid[y][x]
    def set_cell_value(self,x,y,value):
        self.__grid[y][x] = value        
    def winning(self):
        self.__live_points +=1
    def losing(self):
        self.__live_points -= 1

    def right_choice(self):
        import random
        choose_list = [0,0,1]
        # for i in range(3):
        #     choose = random.randint(0,5)
        #     choose_list.append(choose)
        print(choose_list)
        return choose_list

    def play_again(self,x,y):
        if x in [1,2] and y ==  2:
            return 1
        elif x in [3,4]  and y == 2 :
            return 0


    def OK (self,x,y):
        ok_botton_pos_x = 5
        ok_botton_pos_y = 0
        if x == ok_botton_pos_x and y == ok_botton_pos_y:
            return True
        else:
            return False
    
    def count_place(self):
        num_x = 0
        for i in self.__grid[2]:
            if i == 'X':
                num_x += 1
        return num_x

    def clear_grid(self):
        self.__grid = [[0 for x in range(6)] for y in range(3)]

class Namtao :
    def __init__(self,player):
        """Initilize my Namtao Class
        """
        self.player = player
        self.game_id = 2
        self.count_play =0
        self.board = Board(self.player.balance)
    def result(self):
        """ Update num_play and num_win of player
        """
        win_value =self.board.life_point
        for time in range(self.count_play):
            self.player.update_num_play(self.game_id)
        self.player.update_num_win(self.game_id,-(self.player.balance-win_value))
        self.player.update_balance(-(self.player.balance-win_value))
    def main(self): 
        """ Method to run this game
        """
        import pygame
        # from OO_numtao import Board
        pygame.init()
        screen = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption("NUM TAO POO PLA")
        font = pygame.font.SysFont("comicsans" , 64 ,True)
        # board = Board(self.player.balance)
        choose = self.board.right_choice()
 
        run = True
        while run :
            want_bet = font.render("Place your bet !" , 1 , (255,255,255))
            screen.blit(want_bet , (20,20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.board.get_game_over():
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        self.board.get_mouse(pos[0]//150 , pos[1]//150 , choose , screen)
                        # board.print_grid()
                if event.type == pygame.MOUSEBUTTONDOWN and self.board.get_game_over():
                    if pygame.mouse.get_pressed()[0]:
                        screen.fill((0,0,0))
                        self.board.clear_grid()
                        pos = pygame.mouse.get_pos()
                        # print(f"{pos[0]//150} {pos[1]//150}")
                        self.board.get_mouse(pos[0]//150 , pos[1]//150 , choose , screen)
                        if self.board.get_game_over():
                            play_again = self.board.play_again(pos[0]//150 , pos[1]//150)
                            if play_again == 1 :
                                self.count_play +=1
                                self.board.set_place_bet(True)
                                self.board.set_game_over(False)
                                choose = self.board.right_choice()   
                
                            elif play_again == 0 :
                                self.count_play +=1
                                self.result()
                                run = False
                        

                # if event.type == pygame.KEYDOWN:        
                #     if event.key == pygame.K_SPACE and board.get_game_over():
                #         board.clear_grid()
                #         board.set_place_bet(True)
                #         board.set_game_over(False)
                #         choose = board.right_choice()
                #         screen.fill((0,0,0))
                        
            if self.board.end_game():
                print("You Die ")
                font = pygame.font.SysFont("comicsans" , 64 ,True)
                game_over = font.render("You lose" , 1 , (255,255,255))
                screen.blit(game_over , (450,150))
                self.result()
                break
            self.board.draw(screen,choose)
            pygame.display.update()
        pygame.quit()

player = Player('Kao',10)
namtao1 = Namtao(player)
namtao1.main()
