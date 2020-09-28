# texxt_name = input("Enter data file : ")
# data = open(texxt_name).read().splitlines()
# sum_ = 0
# list_score = []
# list
# print(f"Name                  Credit           Grade")
# for i in data :
#     i = i.split(",")
#     for j in i :
#         print(f" {j:>5} " ,end=  "")
    
#     print()
# for j in i :
#     sum_ += int(j)
# list_score.append(sum_)
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
hand =[]

############? Create The Random Deck ############
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' ' + suit
        deck += [card]
