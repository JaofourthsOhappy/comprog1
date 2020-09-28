# def get_input():
#     choose = input('')
#     if choose != 'rock' or choose != 'paper' or choose != 'sissors':
#         print("invalid input")
#     return choose
# def rule(player,computer):
#     c = 'computer wins!'
#     p = 'player wins!'
#     if player == 'rock' and computer == 'paper' :
#         return c
#     elif player == 'rock' and computer == 'sissors':
#         return p
#     elif player == 'paper' and computer== 'rock':
#         return p
#     elif player == 'paper' and computer == 'sissors':
#         return c
#     elif player == 'sissors' and computer == 'paper':
#         return p
#     else:
#         return c

# p1 = get_input()
# c1 = get_input()
# print(f'player choose {p1}')
# print(f"Computer choose {c1}")

def cheak_valid_input(s):
    if s == 'rock':
        return True
    elif s == 'sissors':
        return True
    elif s == 'paper':
        return True
    else :
        return False
def convert_to_num(s):
    if s == 'rock':
        return 0
    elif s == 'sissors':
        return 1
    elif s == 'paper':
        return 2
    else :
        print("Error")
def convert_to_string(n):
    if n == 0:
        return 'rock'
    elif n== 1:
        return 'paper'
    else :
        return 'sissors'
def game_decision(player,computer):
    if player == computer:
        print("Both tie")
    elif (player +1)%3 ==computer:
        print("Computer win!")
    else:
        print("player win!")
valid = False 
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = cheak_valid_input(player_choice)
    if valid == False:
        print('Invalid input.Try again')

import random
computer_choice_num = random.randint(0,2)
player_choice_num = convert_to_num(player_choice)
computer_choice = convert_to_string(computer_choice_num)
print(f"player choose {player_choice}")
print(f"computer choose {computer_choice}")
game_decision(player_choice_num,computer_choice_num)
# rock=0 paper=1 sissors =2


"""
if player_choice_num == 0:
    if computer_choice_num ==0:
        print("Both tie!")
    elif computer_choice_num == 1:
        print("Computer win!")
    else :
        print("Player win!")
elif player_choice == 1:
    if computer_choice_num ==1:
        print("Both tie!")
    elif computer_choice_num == 2:
        print("Computer win!")
    else :
        print("Player win!")
else :
    if computer_choice_num ==2:
        print("Both tie!")
    elif computer_choice_num == 0:
        print("Computer win!")
    else :
        print("Player win!")
"""