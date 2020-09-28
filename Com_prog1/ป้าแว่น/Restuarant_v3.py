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
    print("Welcome to SKE restaurant")
    adult = int(input("Enter #adult guests: "))
    if adult > 0:
        age = int(input("Enter average adults' age: "))
    else:
        age = 0
    kid = int(input("Enter #kids: "))
    print("------------------------------------")
    return adult, age, kid

def get_suggested_menu(subject, age):
    sug = str(input(f"Suggested {subject}s' menu (Y/N): "))
    if sug == "Y" or sug == "y":
        if subject == "adult":
            health = str(input("Do you want healthy food (Y/N): "))

            if health == "Y" or health == "y":
                 if age < 30:
                     meat,side = "salmon","rice"
                 elif age >= 30 and age < 50:
                     meat,side = "chicken","salad"
                 elif age >= 50:
                     meat,side = "salmon","salad"
                 print(f"The {subject}s' suggested menu is {meat} and {side}\n")  

            elif health == "N" or health == "n":
                if age < 30:
                    meat,side = "chicken","pasta"
                elif age >= 30 and age < 50:
                    meat,side = "beef","pasta"
                elif age >= 50:
                    meat,side = "chicken","rice"
                print(f"The {subject}s' suggested menu is {meat} and {side}\n")
        else:
            meat,side = "chicken","pasta"
            print(f"The {subject}s' suggested menu is {meat} and {side}\n")        

        ################# want this suggest?? #################
        want_sug = str(input(f"Do you want {subject}s' suggested menu (Y/N): "))
        if want_sug == "Y" or want_sug == "y":
            return meat,side
        elif want_sug == "N" or want_sug == "n":
            print("------------------------------------")
            meat,side = order_entree(subject)
            return meat,side
    elif sug == "N" or sug == "n":
            print("------------------------------------")
            meat,side = order_entree(subject)
            return meat,side

def order_entree(subject):
    meat = str(input(f"Which meat do {subject}s want (beef/chicken/salmon): "))
    side = str(input(f"Which side do {subject}s want (pasta/rice/salad): "))
    print("------------------------------------")
    return meat, side

def update_meat_stock(subject, meat, num, beef, chicken, salmon):
    if subject == "adult":
        meat_use = 200
    elif subject == "kid":
        meat_use = 100

    if meat == "beef":
        beef -= meat_use*num
    elif meat == "chicken":
        chicken -= meat_use*num
    elif meat == "salmon":
        salmon -= meat_use*num

    return beef, chicken, salmon

def update_side_stock(subject, side, num, pasta, rice, veggies):
    if subject == "adult":
        side_use = 300
    elif subject == "kid":
        side_use = 150

    if side == "pasta":
        pasta -= side_use*num
    elif side == "rice":
        rice -= side_use*num
    elif side == "salad":
        veggies -= side_use*num

    return pasta, rice, veggies

def update_bill(subject, meat, side, num, total_bill):
    pay = 0
    if meat == "beef":
        pay += 150
    elif meat == "chicken":
        pay += 100
    elif meat == "salmon":
        pay += 200
    
    if side == "pasta":
        pay += 50
    elif side == "rice":
        pay += 25
    elif side == "salad":
        pay += 30

    if subject == "adult":
        return (pay*num) + total_bill
    elif subject == "kid":
        return ((pay*num)*0.75) + total_bill

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

########################## Main program ################################

adult,age,kid = greet()

print_stock()

if adult > 0:
    print("ADULTS' ORDER")
    meat_adult,side_adult = get_suggested_menu("adult",age)
    adult_bill = update_bill("adult",meat_adult,side_adult,adult,0)
    total_bill = update_bill("adult",meat_adult,side_adult,adult,total_bill)
    print_bill("adult",meat_adult,side_adult,adult,adult_bill,total_bill)

    #################### Update stock ####################
    beef, chicken, salmon = update_meat_stock("adult", meat_adult, adult, beef, chicken, salmon)
    pasta, rice, veggies = update_side_stock("adult", side_adult, adult, pasta, rice, veggies)

if kid > 0:
    print("KIDS' ORDER")
    meat_kid,side_kid = get_suggested_menu("kid",0)
    kid_bill = update_bill("kid",meat_kid,side_kid,kid,0)
    total_bill = update_bill("kid",meat_kid,side_kid,kid,total_bill)
    print_bill("kid",meat_kid,side_kid,kid,kid_bill,total_bill)

    #################### Update stock ####################
    beef, chicken, salmon = update_meat_stock("kid", meat_kid, kid, beef, chicken, salmon)
    pasta, rice, veggies = update_side_stock("kid", side_kid, kid, pasta, rice, veggies)

print_stock()''