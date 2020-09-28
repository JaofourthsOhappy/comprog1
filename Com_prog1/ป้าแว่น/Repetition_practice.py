"""
x = int(input("Please input X: "))
y = int(input("Please input Y: "))
for i in range(x,y+1):
    if i % 2 != 0:
        print(i)
if x %2 == 0 :
    x = x+1
for i in range(x,y+1,2):
    print(i)
status = True
while status:
    for i in range(x,y+1):
        if i%2 != 0:
            print(i)
    status = False
"""
# num = int(input("Input your factorial number: "))
# sum = 1
# for i in range(1,num+1):
#     sum = i*sum
# print(f'{num}! = {sum}')
"""
def factorial(x):
    sum = 1
    for i in range(1,x+1):
        sum = i*sum
    return sum
def combination(n,k):
    result = factorial(n)/(factorial(k)*factorial(n-k))
    return int(result)
n = int(input("n: "))
k = int(input("k: "))
print(f"Combination of {n} choose {k} = {combination(n,k)}")
"""
"""
hour = int(input("Enter numbers of hours: "))
def cal (hour):
    sec = hour*60*60
    return sec
for i in range(1,hour+1):
    count = cal(i) / 20
    cost = count *0.40
    print(f"In {i} hour(s), my factory produces {int(count)} candies, and I make profit of {cost:.2f} Baht.")
"""

# x = int(input("Enter cash in Baht: "))
# n = int(input("Enter N years: "))
# RATE = 0.015
# sum = x
# for i in range(1,n+1):
#     sum = x*((1+RATE)**i)
#     print(f'You will get back {sum:.2f} Baht in {i} years.')
# print(f"At the end, you will earn {sum-x} Baht of interest in {n} years.")
"""
x = int(input('Enter a: '))
y = int(input('Enter b: '))
# status = True
# while status:
#     for i in range(1,a) :
#         if a % i == 0 :
#             lcm1 = a
#     for i in range(1,b) :
#         if  b % i == 0 :
#             lcm2 = b
#     if lcm1 == lcm2 :
#         lcm = lcm1
#         print(f'GCD of {a} and {b} is {lcm}')
#         status = False

def gcd(m,n):
    z=abs(m-n)
    if (m-n)==0:
        return n
    else:
        return gcd(z,min(m,n))
print(f'GCD of {x} and {y} is {gcd(x,y)}')

# """
# import math
# def formula(number):
#     """
#     Get the result of series of numbers, by formula sqrt(n^1+n^2+n^3+...+n^n)
#     :params number is the positive integer
#     :return result of the series
#     >>> formula(2)
#     2.449489742783178
#     >>> formula(5)
#     62.489999199871974
#     >>> formula(1)
#     1.0
#     """
#     sum = 0
#     for i in range(1,number+1):
#         sum = (number**i)+sum
#     value = math.sqrt(sum)
#     return value
# n = int(input("Input n: "))
# result = formula(n)
# print(f"The formula value is {result:.4f}")
# """

# num = int(input("Enter positive number: "))
# print(f"Factors of {num} are")
# sum,count = find_sum_and_num_factors(num)
# factor = list_factors(num)
# print(factor)
# print(f"Sum of {factor} is {sum}")
# print(f"Number of factors is {count}")
# if len(factor) <= 2:
#     print(f"{num} is prime number.")
# else :
#     print(f"{num} is not prime number.")


# goal_amount = int(input("Enter your goal amount: "))
# sum = 0
# day_count = 0
# while True:
#     money_per_day = int(input("Enter money collected today: "))
#     sum += money_per_day
#     day_count += 1
#     if goal_amount > sum :
#         print(f"Day {day_count}: your total is {sum}.  You need {goal_amount-sum} more. ")
#     else:
#         break
# print(f"Congratulations!  You take {day_count} days to reach your goal.")


# def count_digits(number):
#     """
#    Get number of digits in number
#    :params number is an integer
#    :return number of digits in number

#     >>> count_digits(41)
#     2
#     >>> count_digits(-41)
#     2
#     >>> count_digits(1)
#     1
#     """
#     if number <0:
#         number = (-1)*number
#     number = str(number)
#     count = 0
    #         for i in number:
    #                 count+=1
    #         break

    # return count

# number = int(input("Enter number: "))
# num_digits = count_digits(number)
# print(f"There are {num_digits} digits in {number}")

def get_last_digit(n):
    return n%10

# number = int(input("Input number: "))
# num_digits = count_digits(number)
# s = ""
# dig = 10
# i =0
# while True:
#     # print(i)
#     last = get_last_digit(number//(10**i))
#     s += f"{last}x10^{i}"
#     if i+1 >= num_digits :
#         break
#     else:
#         s+= ' + '
#         i+=1
# print(f"{number} = {s}")

# count_h =0
# count_t = 0
# s = 'You entered '
# while True :
#     coin = input("Enter H, T or Q: ")
#     if coin != 'Q' and coin != 'T' and coin != 'H':
#         print('Error! This choice is invalid!!!')
#     elif coin == 'Q':
#         break
#     else:
#             if coin == 'H':
#                 count_h +=1
#             elif coin == 'T':
#                 count_t+= 1
#             s+= f'{coin},'
# if count_t == 0 and count_h == 0:
#     print("You entered nothing.")
# else:
#     print(s)
# print(f"Number of Heads is {count_h}")
# print(f"Number of Tails is {count_t}")

# def define_room (floor):
#     if floor == 1 :
#         room = 'Lobby'
#         level = 'ground'
#     elif floor == 2 :
#         room = 'Emergency Room'
#         level = 'second'
#     elif floor == 3 :
#         room = 'ICU'
#         level = 'third'
#     elif floor == 4:
#         room = 'Pharmacy'
#         level = 'fourth'
#     elif floor == 5:
#         room = 'Ward'
#         level = 'fifth'
#     elif  floor == 6:
#         room = 'Office'
#         level = 'sixth'
#     else:
#         room = ''
#         level = ''
#     return  room , level
    


# teddy = input("Please input room where Teddy is: ")
# while True:
#     guess_floor = int(input("Guess Teddy's floor number: "))
#     room_name ,level_ = define_room(guess_floor)
#     if guess_floor >6 and guess_floor <0 :
#         print(f"There is no floor {guess_floor}.")
#     elif room_name != teddy :
#         print(f"Teddy is not on {level_} floor or in {room_name}.")
#     else :
#         print(f"Teddy is found in {room_name} on {level_} floor.")
#         break


# def list_factors(n):
#     factor = ''
#     for i in range(1,n+1):
#         if n % i == 0 :
#             factor+=f'{str(i)} '
#     return factor
# def find_sum_and_num_factors(n):
#     factor = list_factors(n).split()
#     sum_ = 0
#     count_ = 0 
#     for i in factor:
#         sum_ += int(i)
#         count_ +=1
#     return sum_ ,count_
# num = int(input("Enter positive number: "))
# print(f"Factors of {num} are")
# print(list_factors(num))
# sum_factor, count_factor = find_sum_and_num_factors(num)
# print(f"Sum of {list_factors(num)} is {sum_factor}")
# print(f"Number of factors is {count_factor}")
# if count_factor == 2 :
#     print(f"{num} is prime number.")
# else :
#     print(f"{num} is not prime number.")


# sum = 0
# count = 0
# a = []
# while True :
#     try:        
#         num = float(input("Enter a number (just [Enter] to quit): "))
#     except ValueError:
#         if count <1 :
#             print("Nothing to do.")     
#             break   
#         else:   
#             avg = sum/count
#             print(f"The maximum is {max(a):.2f}")
#             print(f"The minimum is {min(a):.2f}")
#             print(f"The average is {avg:.2f}")
#             break

#     sum+= num
#     count+=1  
#     a.append(num)

# depth = int(input("Enter the depth of the well: "))
# can_jump = int(input("Enter the height the frog can jump: "))
# slip = int(input("Enter the height the frog slips down: "))
# day = 1
# remain = 0
# while True :
#     if can_jump>=depth:
#         print(f"The frog can escape the well on day {day}.")
#         break
#     elif can_jump - slip == 0 :
#         print("The frog will never escape from the well.")
#         break
#     else:
#         remain = depth-can_jump+slip     
#         print(f"On day {day} the frog leaps to the depth of {depth-can_jump} meters.")
#         print(f"At night he slips down to the depth of {remain} meters.")
#     depth = remain 
#     day+=1 

# sum = 0
# count = 1
# list_score = []
# while True :
#     try:        
#         score =int(input("Enter student score (or ENTER to finish): "))

#     except ValueError:
#         l = 1
#         list_score.sort(reverse = True)
#         for i in list_score:
#             print(f"Rank #{l}: {i}")
#             l+=1
#         break
#     sum+= score
#     count +=1
#     list_score.append(score)
    # max = score
    # min = score
    # if score > max :
    #     max = score
    # if score < max:
    #     min = score


# def decrypt(msg):
#     msg = msg[::-1]
#     code = []
#     for charactor in msg:
#         if charactor == 'O':
#             code.append('G')
#         elif charactor == 'D':
#             code.append("O")
#         elif charactor == 'G':
#             code.append("D")
#         else :
#             code.append(charactor)

#     return "".join(code)
# print(decrypt("ONINRDM GDDO"))

