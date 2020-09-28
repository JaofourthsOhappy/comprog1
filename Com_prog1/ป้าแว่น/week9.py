def display_final(list_,namelist):
    count = 0
    for i in namelist:
        print(f"({i}: {list_[count]:.2f})," , end = ' ')
        count+=1
    print()
    # for i in range(len(list_)+):
    #     print(f"({namelist[i]} : {list_[i]})," , end = '')
    print(f"Average donation = {(sum(list_)/count):.2f}")

def display_list(total_donation, money , milk ):
    print("Current donation: ")
    print(f"Money ({len(money)} donators) = {sum(money):.2f} Baht")
    print(f"Milk ({len(milk)} donators) = {int(sum(milk))} packs ")
    print(f"Total donation = {total_donation:.2f} Baht")
    print()
def update_milk_list(amount , name , milk_name_list , milk_list , money_name_list , money_list):
    pack = amount // 1000
    milk_list.append(pack)
    money = amount % 1000
    if money == 0 :
        milk_name_list.append(name)
    else:
        milk_name_list.append(name)
        money_name_list.append(name)        
        money_list.append(money)


money_list = []
amount = float(input("Enter donation amount: "))
money_namelist = []
total_donation = 0
milk_list = []
milk_namelist = []
while amount >0 :
    choice = input("Enter donation choice (m/k): ")
    name = input ("Enter your name: ")
    if choice == "m" : 
        money_list.append(amount)
        money_namelist.append(name)
        total_donation += amount
    elif choice == 'k':
        update_milk_list(amount , name , milk_namelist,milk_list , money_namelist,money_list )
        total_donation += amount
    else:
        print("Wrong choice. Start over.")

    display_list(total_donation , money_list , milk_list )
    amount = float(input("Enter donation amount: "))   
print("Final donation:")
print("Money (Baht):")
display_final(money_list, money_namelist)
print("Milk (pack):")
display_final(milk_list,milk_namelist)
