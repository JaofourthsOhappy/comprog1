ONE_MEAT_SERVE = 200
ONE_SIDE_SERVE = 300
GRAMS_TO_KG = 1000.0

beef = 2*1000    # 2kg
chicken = 5*1000 # 5kg
salmon = 3*1000  # 3kg
pasta = 5*1000   # 5kg
rice = 5*1000    # 5kg
veggies = 5*1000 # 5kg

total_bill = 0

def greet():
    adult = int(input("Enter #adult guests: "))
    adult_avg = int(input("Enter average adults' age: "))
    kid = int(input("Enter #kids: "))
    return adult,adult_avg,kid

def get_suggested_menu(subject, age):
    print(f"{str(subject.upper())}' ORDER")
    suggest = input(f"Suggested {subject}' menu (Y/N): ")
    if suggest == 'Y' :
        if subject != 'kids':
            healthy = input(f"Do you want healthy food (Y/N): ")
            if healthy == 'Y':
                if age<30 :
                    meat = 'salmon'
                    side = 'rice'
                elif 30 <= age <50:
                    meat = 'chicken'
                    side = 'salad'
                else :
                    meat = 'salmon'
                    side = 'salad'
            else :
                if age< 30 or subject == 'kids':
                    meat = 'chicken'
                    side = 'pasta'
                elif 30 <= age <50:
                    meat = 'beef'
                    side = 'pasta'
                else:
                    meat = 'chicken'
                    side = 'rice'
            print(f"The {subject}' suggested menu is {meat} and {side}")
        else:
            meat = 'chicken'
            side = 'pasta'
            print(f"The {subject}' suggested menu is chicken and pasta")
        print("")
        want_suggest = input(f"Do you want {subject}' suggested menu (Y/N):")
        if want_suggest == 'Y':
            return meat,side
        else :
            print("------------------------------------")
            meat,side = order_entree(subject)
            return meat,side 
    else:  
        print("------------------------------------")
        meat,side = order_entree(subject) 
        return meat,side
def order_entree(subject):
    meat = input(f"Which meat do {subject} want (beef/chicken/salmon): ")
    side = input(f"Which side do {subject} want (pasta/rice/salad): ")
    print("------------------------------------")
    return meat,side
    
def update_meat_stock (subject, meat, num, beef, chicken, salmon):
    if subject == 'adult':
        use = 200
    else :
        use = 100
    if meat == 'chicken':
        chicken = chicken - (num*use)
    elif meat == 'salmon':
        salmon = salmon - (num*use)
    else:
        beef = beef-(num*meat)
    return chicken ,salmon,beef
   
def update_side_stock (subject, side, num, pasta, rice, veggies):
    if side == 'pasta':
        pasta = pasta-(num*side)
        return pasta
    elif side == 'rice':
        rice = rice-(num*side)
        return rice
    else:
        veggies = veggies -(num*side)
        return veggies
def update_bill (subject, meat, side, num, total_bill):
    price_meat = 0
    price_side =0
    if meat == 'salmon':
        price_meat = 200
    elif meat == 'chicken':
        price_meat = 100
    else :
        price_meat = 150
    if side == 'pasta':
        price_side = 50
    elif side == 'rice':
        price_side = 25
    else:
        price_side = 30
    if subject == 'kids':
        total = 0.75*num*(price_meat + price_side) +total_bill
    else: 
        total = num*(price_meat + price_side) +total_bill
def print_bill(subject, meat, side, num, bill, total_bill):
    print(f"The {subject}s' order {num} {meat} and {side}")
    print(f"The {subject}s' order costs {bill:.2f} Baht")
    print(f"Total payment is {total_bill:.2f} Baht")
    print("------------------------------------")
def print_stock():
    print("List of food stock:")
    print(f"Beef = {beef/GRAMS_TO_KG:.2f} kg")
    print(f"Chicken = {chicken/GRAMS_TO_KG:.2f} kg")
    print(f"Salmon = {salmon/GRAMS_TO_KG:.2f} kg")
    print(f"Pasta = {pasta/GRAMS_TO_KG:.2f} kg")
    print(f"Rice = {rice/GRAMS_TO_KG:.2f} kg")
    print(f"Veggies = {veggies/GRAMS_TO_KG:.2f} kg")
    print("------------------------------------")
print("Welcome to SKE restaurant")
adult,adult_avg,kid = greet()
print_stock()
if adult > 0:
    meat_adult,side_adult = get_suggested_menu("adult",adult_avg)
    adult_bill = update_bill("adult",meat_adult,side_adult,adult,0)
    total_bill = update_bill("adult",meat_adult,side_adult,adult,total_bill)
    print_bill("adult",meat_adult,side_adult,adult,adult_bill,total_bill)
    beef, chicken, salmon = update_meat_stock("adult", meat_adult, adult, beef, chicken, salmon)
    pasta, rice, veggies = update_side_stock("adult", side_adult, adult, pasta, rice, veggies)

if kid >0:
    meat_kid,side_kid = get_suggested_menu("kid",0)
    kid_bill = update_bill("kid",meat_kid,side_kid,kid,0)
    total_bill = update_bill("kid",meat_kid,side_kid,kid,total_bill)
    print_bill("kid",meat_kid,side_kid,kid,kid_bill,total_bill)
    beef, chicken, salmon = update_meat_stock("kid", meat_kid, kid, beef, chicken, salmon)
    pasta, rice, veggies = update_side_stock("kid", side_kid, kid, pasta, rice, veggies)
print_stock()