import math,sys

# Ex.1
def is_even(number):
    if number % 2 == 0:
        return True
    else :
        return False

# Ex.2
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else :
        return False

# Ex.3
def interval_intersect(a,b,c,d):
    AB = set(range(a,b+1))
    CD = set(range(c,d+1))
    if len(AB.intersection(CD)) != 0 :
        return True
    else :
        return False

# Ex.4
def print_digits():
    number = int(input())
    if 0 <= number < 100:
        print(f"The tens digit is {number//10} and the ones digits is {number%10}")
    else :
        sys.exit("Error: Input is not a two-digit number.")

# Ex.5
def smaller_root():
    a = float(input())
    b = float(input())
    c = float(input())
    d = (b**2)-(4*a*c)
    if d > 0:
        x = (-b + (math.sqrt(d)))/(2*a)
        y = (-b - (math.sqrt(d)))/(2*a)
        return x,y
    elif d == 0:
        x = (-b + (math.sqrt(d)))/(2*a)
        return x
    else :
        print("Error: No real solutions")
        return None

# Ex.6
def there_is_odd(x,y,z):
    number = [x,y,z]
    for i in number:
        if i % 2 == 1:
            odd = i
    if odd != []:
        print(f"There is an odd number whose value is {odd} ")
    else :
        print("There is no odd number")

# Ex.7
def list_all_odds(w,x,y,z):
    number = [w,x,y,z]
    odd = []
    for i in number:
        if i % 2 == 1:
            odd.append(i)
    if odd != []:
        odd.sort()
        for i in odd:
            print(f"There is an odd number whose value is {i} ")
    else :
        print("There is no odd number")

# Ex.8
def max_of_three(x,y,z):
    number = [x,y,z]
    number.sort()
    print(f"The max value is {number[2]}")