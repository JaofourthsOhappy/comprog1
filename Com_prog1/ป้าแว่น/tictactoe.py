import pygame
from grid import *

SQUARESIZE = 100
NUM_ROWS =3
NUM_COLS = 3

WIDTH  = (NUM_COLS+1) * SQUARESIZE
HEIGHT = NUM_ROWS * SQUARESIZE

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.SysFont("comicsans" , 20 ,True)

board = grid()
run = True 
player = "X"
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not board.get_game_over():
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                board.get_mouse(pos[0] // 100 , pos[1] // 100 , player)
                if board.get_switch_player() == True:
                    if player == 'X' :
                        player = 'O'
                    else:
                        player = 'X'
                board.print_grid()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE and board.get_game_over():
                board.clear_grid()
                board.set_game_over(False)
                board.set_winner('None')
                player = 'X'
    screen.fill((0,0,0))
    if board.get_game_over():
        text = font.render(board.get_winner()+ ' wins!' , 1 , (255,255,255))
        screen.blit(text,(WIDTH - int(SQUARESIZE*0.75) , int(HEIGHT/2)))
    board.draw(screen)
    pygame.display.update()
pygame.quit()