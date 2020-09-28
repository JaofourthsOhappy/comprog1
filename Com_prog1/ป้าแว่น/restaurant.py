def order(name,age):
    print(f"{name}' ORDER")
    s_menu = input(f"Suggested {name}' menu (Y/N): ")
    if s_menu == 'Y': 
        
        healthy = input("Do you want healthy food (Y/N): ")
        if healthy == 'Y' :
            if 0<age <30:
                meat = 'salmon'
                side = 'rice'
            elif 30<= age <50:
                meat = 'chicken'
                side = 'salad'
            else:
                meat = 'chicken'
                side = 'rice' 
        else:
            if 0<age<30 :
                meat = 'chicken'
                side = 'pasta'
            elif 30<= age<50:
                meat = 'beef'
                side= 'pasta'
            else:
                meat= 'chicken'
                side = 'rice'
        print("")
        print(f"The {name}' suggested menu is {meat} and {side}")   
        want_s = input("Do you want adults' suggested menu (Y/N): ")
        if want_s == 'Y':
            return meat,side     
        else:
            print("------------------------------------")
            meat = input("Which meat do adults want (beef/chicken/salmon): ")
            side = input("Which side do adults want (pasta/rice/salad): ")   
    else:
        print("------------------------------------")
        meat = input("Which meat do adults want (beef/chicken/salmon): ")
        side = input("Which side do adults want (pasta/rice/salad): ")
    return meat,side
def cal_price(food):
    beef = 150
    chicken = 100
    salmon = 200
    pasta =50
    rice =25
    veggies =30   
    if food =='beef':
        return beef
    elif food== 'chicken':
        return chicken
    elif food == 'salmon':
        return salmon
    elif food == 'pasta':
        return pasta
    elif food == 'rice':
        return rice
    else :
        return veggies
# def food_list(meat,side):
 
print("Welcome to SKE restaurant")
adult= int(input("Enter #adult guests: "))
adult_avg = int(input("Enter average adults' age: "))
kid = int(input("Enter #kids: "))
print("------------------------------------")
# print(food_list())
if adult>0 or kid>0 :    
    meat_a,side_a = order("adults",adult_avg)
    print(f"The adults' order {adult} {meat_a} and {side_a}")
    price = adult*(cal_price(meat_a)+cal_price(side_a))
    print(f"The adults' order costs {price:.2f} Baht")
    total = price
    print(f"Total payment is {total:.2f} Baht")
    meat_k,side_k = order("kids",0)
    print(f"The kids' order {kid} {meat_k} and {side_k}")
    price = kid*(cal_price(meat_k)+cal_price(side_k))

