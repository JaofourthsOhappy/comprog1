# constant
STAY_VAL = 16
#create deck
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
class Deck : 
    def __init__(self, deck = []):
        self.deck = deck
    def initialize(self):
        for rank in RANKS:
            for suit in SUITS:
                card = rank + ' ' + suit
                self.deck += [card]
        return self.deck
    def shuffle(self):
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
        self.hand = hand
        self.hand_value = value
        self.deck = deck

    def cal_value(self):
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
        for i in range(n):
            self.hand.append(self.deck.pop())
        return self.hand

    def display(self,num =0 ):
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
        hand_val = self.cal_value()
        if hand_val < STAY_VAL:
            return True
        else:
            return False

    def black_jack(self):
        hand_val = self.cal_value()
        if hand_val == 21 :
            return True
        else:
            return False
    