# status = True
# while status :
#         user_input = input ("Enter  your Age: ")
#         try:
#                 val = int(user_input)
#                 print("Yes input string is an Integer.")
#                 print("Input number value is: ", val)
#                 status = False
#         except ValueError:
#                 print("That's not an int!")

# for i in range(-6,5,2):
#         print(i, end = ' ')

# for i in range(-6,5,2):
#         print(f"{i}  " )


def print_multiple_k_for (m,n,k):
        sum = 0
        count = 0
        for i in range(m,n+1):
                if i % k == 0 :
                        print(i , end = ' ')              
                        sum = sum+i
                        count += 1 
        print("")
        return sum,count
def print_multiple_k_while(m,n,k):
        sum = 0
        count = 0
        i = m
        while  i <  n+1 :
                if i % k == 0:
                        print(i, end = ' ')
                        sum = sum+i
                        count += 1
                i +=1
        print("")
        return sum ,count
"""
m  = int(input("Enter m: "))
n = int(input("Enter n: "))
k = int(input("Enter positive k:"))
#sum, count =print_multiple_k_for(m,n,k)
sum, count =print_multiple_k_while(m,n,k)
print(f"There are {count} printed numbers")
print(f"Sum of printed number = {sum}")
"""
def dice_loop_sentinel():
        count = 0
        sum =0
        dice = int(input("Roll a dice. Enter point: "))       
        while dice>0:
                count += 1
                sum += dice
                dice = int(input("Roll a dice. Enter point: "))
        print(f"You rolled {count} times")
        print(f"Sum of dice points is {sum}")

def dice_loop_sentinel_2():
        count = 0
        sum =0
        dice = int(input("Roll a dice. Enter point: "))       
        while dice>=0:
                if dice > 6  or dice == 0:
                        print("Invalid point. is between 1-6")
                else :
                        count += 1
                        sum += dice
                dice = int(input("Roll a dice. Enter point: "))
 
        print(f"You rolled {count} times")
        print(f"Sum of dice points is {sum}")


def dice_loop_break():
        count = 0
        sum = 0
        dice = int(input("Roll a dice. Enter point: "))
        while True:
                if dice >0 :
                        sum += dice
                        count += 1
                        dice = int(input("Roll a dice. Enter point: "))
                else:
                        break
        print(f"You rolled {count} times")
        print(f"Sum of dice points is {sum}")

def dice_loop_break_2():
        count = 0
        sum = 0
        dice = int(input("Roll a dice. Enter point: "))
        while True:
                if dice >=0 :
                        if dice > 6 or dice ==0:
                                print("Invalid point. is between 1-6")
                        else:
                                sum += dice
                                count += 1
                        dice = int(input("Roll a dice. Enter point: "))
                else:
                        break
        print(f"You rolled {count} times")
        print(f"Sum of dice points is {sum}")
#dice_loop_break_2()
dice_loop_sentinel_2()