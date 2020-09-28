def check_valid_input(s):
    """
    >>> check_valid_input("gun")
    True
    >>> check_valid_input("zombie")
    True
    >>> check_valid_input("paruj")
    False
    """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "spock":
        return True
    elif s == "zombie":
        return True
    elif s == "gun":
        return True
    elif s == "lizard":
        return True
    else:
        return False

def convert_to_num(s):
    """
    >>> convert_to_num("paruj")
    Error: should not reach this if input is a valid one
    >>> convert_to_num("lizard")
    6
    >>> convert_to_num("gun")
    5
    """
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "zombie":
        return 4
    elif s == "gun":
        return 5
    elif s == "lizard":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """
    >>> convert_to_string(5)
    'gun'
    >>> convert_to_string(60)
    Error: should not reach this if input is a valid one
    >>> convert_to_string(6)
    'lizard'
    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    elif n == 3 :
        return "spock"
    elif n == 4:
        return "zombie"
    elif n == 5:
        return "gun"
    elif n == 6 :
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    """
    >>> game_decision(1,2)
    Computer wins!
    >>> game_decision(2,1)
    Player wins!
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(4,0)
    Computer wins!
    >>> game_decision(4,2)
    Computer wins!
    >>> game_decision(3,0)
    Player wins!
    >>> game_decision(5,1)
    Computer wins!
    >>> game_decision(3,6)
    Computer wins!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 7) == computer_choice_num or (((player_choice_num + 3) % 7)) == computer_choice_num or (((player_choice_num + 5) % 7)) == computer_choice_num: 
        print("Computer wins!")
    else:
        print("Player wins!")

    
    
# get an input from a player and validate
def main():    
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    # random a response from a computer and print out player and computer choices
    import random
    computer_choice_num = random.randint(0, 6)
    computer_choice = convert_to_string(computer_choice_num) 
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)
    game_decision(player_choice_num, computer_choice_num)
# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2

# do this


# instead of this ugly if-elif-else nested block
"""
if player_choice_num == 0:
    if computer_choice_num == 0:
        print("Both ties!")
    elif computer_choice_num == 1:
        print("Computer wins!")
    else:
        print("Player wins!")
elif player_choice_num == 1:
    if computer_choice_num == 1:
        print("Both ties!")
    elif computer_choice_num == 2:
        print("Computer wins!")
    else:
        print("Player wins!")
else:
    if computer_choice_num == 2:
        print("Both ties!")
    elif computer_choice_num == 0:
        print("Computer wins!")
    else:
        print("Player wins!")
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()



