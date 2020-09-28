adult = int(input("How many adults?: "))
kid = int(input("How many children?: "))
day = input("Day (su,mo,tu,we,th,fr,sa): ")
if day != 'su' and day!= 'mo' and day != 'tu' and day!='we' and day!='th' and day!='fr' and day!='sa' and adult <=0 and kid<= 0 :
    print("Incorrect input!")
else:    
    adult_price = adult*500
    kid_price = kid*250
    print(f"{adult} adults = {adult}x500 = {adult_price}")
    print(f"{kid} children = {kid}x250 = {kid_price}")
    if day == 'tu':    
            discount = (adult_price+kid_price)*0.25
            print(f"Tuesday discount 25% = ({adult_price} + {kid_price}) x 25% = {discount:.2f}")
            total = (adult_price+kid_price)-discount
            print(f"Total price is {total:.2f} Baht.")
    elif day == 'we' :
        discount = (adult_price+kid_price)*0.50
        print(f"Wednesdat discount 50% = ({adult_price} + {kid_price}) x 50% = {discount:.2f}")        
        if kid_price >= 1000:
            kid_discount = kid_price*0.20
            print(f"Wednesday children over 1000 discount 20% = {kid_price} x 20% = {kid_discount:.2f}")
            total = (adult_price+kid_price) - (discount+kid_discount)
            print(f"Total price is {total:.2f} Baht.")
        else :
            total = (adult_price+kid_price)-discount
            print(f"Total price is {total:.2f} Baht.")
    else:
        total = (adult_price+kid_price)
        print(f"Total price is {total:.2f} Baht.")