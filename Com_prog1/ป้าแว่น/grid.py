import pygame 

SQUARESIZE = 100
NUM_ROWS =3
NUM_COLS = 3

letter_x = pygame.image.load('x.png')
letter_o = pygame.image.load('o.png')
class grid : 
    def __init__(self):
        self.__grid_lines = [ ((0,100) , (300,100)) ,
                                         ((0,200) , (300,200)),
                                         ((100,0) ,(100,300)),
                                         ((200,0) , (200,300))]
        self.__grid = [[0 for x in range(3)] for y in range(3)]
        self.__switch_player = True
        self.__game_over = False
        self.__winner = 'None'

    def draw(self, screen):
        for line in self.__grid_lines:
            pygame.draw.line(screen ,(255,255,255) , line[0] , line[1] , 2) 
        for y in range (len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.get_cell_value(x,y) == 'X':
                    screen.blit(letter_x , (x*SQUARESIZE , y* SQUARESIZE))
                elif self.get_cell_value(x,y) == 'O' :
                    screen.blit(letter_o , (x*SQUARESIZE , y * SQUARESIZE))

    def get_mouse (self , x , y , player):
        if self.get_cell_value(x,y) == 0:
            self.__switch_player = True
            if player == 'X':
                self.set_cell_value(x,y , 'X')
            elif player == 'O':
                self.set_cell_value(x,y,'O')
            self.check_grid(x,y, player)
        else: 
            self.__switch_player = False

    def is_grid_full(self) :
        for row in self.__grid:
            for value in row :
                if value == 0:
                    return False
        return True

    def check_grid(self, x, y, player):
        turn = 0
        for i in self.__grid :
            for j in i :
                if j != 0 :
                    turn+= 1
        if turn == 9 :
            self.__game_over = True
            self.__winner = 'None'

        for i in range(2):
            if self.__grid[i][0] == self.__grid[i][1] == self.__grid[i][2]  and self.__grid[i][0] != 0:
                self.__game_over = True
                self.__winner = player

        for j in range(2):
            if self.__grid[0][j] == self.__grid[1][j] == self.__grid[2][j] and self.__grid[0][j] != 0:
                self.__game_over = True
                self.__winner = player
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] and self.__grid[0][0] != 0:
                self.__game_over = True
                self.__winner = player
        if self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] and self.__grid[0][2] != 0:
                self.__game_over = True
                self.__winner = player


    def get_winner(self):
        return self.__winner
    def get_game_over(self):
        return self.__game_over 
    def set_winner(self , value):
        self.__winner = value
    def set_game_over(self ,value):
        self.__game_over = value
    def print_grid(self) :
        for row in self.__grid :
            print(row)
    def clear_grid(self):
        self.__grid  = [[0 for x in range(3)] for y in range(3)]
    def get_cell_value(self ,x ,y):
        return self.__grid[y][x]
    def set_cell_value(self, x, y , value):
        self.__grid[y][x] = value
    def get_switch_player(self):
        return self.__switch_player
