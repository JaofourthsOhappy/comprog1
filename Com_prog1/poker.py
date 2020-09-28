card = input("Cards: ")
card_sprit = card.split()
if ( 'A' and 'J' and 'K' and 'Q' ) not in card_sprit:
    if (len(set(card_sprit))) == 2 and card_sprit.count(card_sprit) == 2:
        print('Saito got "Full house"')
    elif (len(set(card_sprit))) == 2:
        print('Saito got "Four of a kind"')
    elif (len(set(card_sprit))) == 3:
        print('Saito got "Three of a kind"')
    else:
        print('Saito got "High Card" ')
else:
    if (len(set(card_sprit))) == 3 and card_sprit.count() == 2:
        print('Saito got "Full house"')
    elif (len(set(card_sprit))) == 2:
        print('Saito got "Four of a kind"')
    elif (len(set(card_sprit))) == 3:
        print('Saito got "Three of a kind"')
    
    