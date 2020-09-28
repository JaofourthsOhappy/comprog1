# def ticket_price(num,zone):
#     zone = zone.upper()
#     if  zone == 'A':
#         total = 5800 * num
#     elif zone == 'B':
#         total = 4500* num 
#     elif zone == 'C':
#         total = 3500* num
#     elif  zone == 'D':
#         total = 2000 * num
#     return total

# ticket = int(input("How many tickets?: "))
# zone = input('Which zone? (A/B/C/D): ')
# print(f"Total price is {ticket_price(ticket,zone)} Baht.")

def ask_user():
    ticket = int(input("How many tickets?: "))
    zone = input('Which zone? (A/B/C/D): ')
    code = input('Do you have promotional code? (Y/N): ')
    code =code.upper()
    if code == 'Y':
        promo_code = input('Enter promo code: ')
        return ticket ,zone,promo_code
    else:
        promo_code = ''
        return ticket,zone,promo_code
def ticket_price(num,zone):
    zone = zone.upper()
    if  zone == 'A':
        price = 5800 * num
    elif zone == 'B':
        price = 4500* num 
    elif zone == 'C':
        price = 3500* num
    elif  zone == 'D':
        price = 2000 * num
    return price
def discount_tic(price,code):
    if code == 'HAVEFUN45':
        total = price*0.55
    elif code == 'HAVEFUN20':
        total = price*0.80
    elif  code == 'HAVEFUN10':
        total = price* 0.90
    else :
        total = price
    return total
#ticket, zone, code = ask_user()
ticket,zone,code = ask_user()
cost = ticket_price(ticket,zone)
i = discount_tic(cost,code)
print(f"Total price is {i:.2f} Baht.")