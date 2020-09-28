ADULT_FEE = 500
CHILD_FEE = 250
sum_children_cost = 0
sum_adult_cost = 0
tuesday_discount = 0
wednesday_discount = 0
more_than_1000_on_wed_discount = 0
#This function is to return the discount rate for different days condition
def discount_rate(condition):   
    tuesday_discount = 0
    wednesday_discount = 0
    more_than_1000_on_wed_discount = 0
    if condition == 'tu':
        return 0.25
    elif condition == 'we':
        return 0.50
    elif condition == "over1000":
        return 0.20
    else:
        return 1

def is_valid_day(day):
#This function to check if input day is valid
    return day == 'su' or day == 'mo' or day == 'tu' or day == 'we' or day == 'th' or day =='fr' or day == 'sa'
def cal_children_cost(children):
    return children*250
def cal_adult_cost(adult):
#This function is to calculate and return the all adult price calculated
    return adult*500

def print_tuesday(sum_adult_cost,sum_children_cost,discount_rate):
#This function is to calculate and print Tuesday price
    tuesday_discount = (sum_adult_cost + sum_children_cost)* discount_rate('tu')
    print(f'Tuesday discount 25% = ({sum_adult_cost} + {sum_children_cost}) x 25% = {tuesday_discount:.2f} ')

def print_wednesday(sum_adult_cost,sum_children_cost,discount_rate,more_than_1000_on_wed_discount):  
#This function is to calculate and print Wednesday price
    wednesday_discount = (sum_adult_cost + sum_children_cost) *discount_rate('we')
    print(f'Wednesday discount 50% = ({sum_adult_cost} + {sum_children_cost}) x 50% = {(sum_adult_cost + sum_children_cost) * 0.50:.2f}')   
    if sum_children_cost >=1000:
        more_than_1000_on_wed_discount = sum_children_cost * discount_rate("over1000")
        print(f'Wednesday children over 1000 discount 20% = {sum_children_cost} x 20% = {(sum_children_cost) * 0.20:.2f}')
    print(f'Total price is {sum_children_cost + sum_adult_cost - wednesday_discount - more_than_1000_on_wed_discount  :.2f} Baht.')


adult = int(input("How many adults?: "))
children = int(input("How many children?: "))
day = input("Day (su,mo,tu,we,th,fr,sa): ")
if is_valid_day(day) == True:
    sum_children_cost = cal_children_cost(children)
    sum_adult_cost = cal_adult_cost(adult) 
    print(f"{adult} adults = {adult}x500 = {sum_adult_cost}")   
    print(f"{children} children = {children}x250 = {sum_children_cost}")
    # print(f"Total price is {sum_adult_cost+sum_children_cost:.2f} Baht.")
    # discount_rate = discount_rate(day)
    if day == 'tu':
        print_tuesday(sum_adult_cost,sum_children_cost,discount_rate)
    if(day == 'we'):
        print_wednesday(sum_adult_cost,sum_children_cost,discount_rate,more_than_1000_on_wed_discount)
else:
    print(f'Incorrect input!')
