def f(n):
    """
    Compute value of function f
    :params n: is the number to compute value of function f
    :return: value of function f
    >>> f(1)
    1.0
    >>> f(2)
    1.5
    >>> f(3)
    1.8333333333333333
    >>> f(10)
    2.9289682539682538
    """
    if n >=1 and n <100 :
        return 1/n

#* n = int(input("Input n: "))
#* print(" n | f(n)")
#* print("---+------")
#* sum_ = 0
#* for i in range(1,n+1):
#*     sum_ += f(i)
#*     print(f"{i:^3}| {sum_:.3f}")


def printSleepTime(start_time,duration):
    """
    Print sleeping time starting from start_time and lasting for duration minutes
    :params start_time: time to start sleeping
            duration: duration of sleeping
    >>> printSleepTime(1,5)
    1 min
    2 min
    3 min
    4 min
    5 min
    >>> printSleepTime(6,2)
    6 min
    7 min
    >>> printSleepTime(11,3)
    11 min
    12 min
    13 min
    """
    for i in range(start_time, start_time+duration):
        print(f"{i} min")
# ? nap_time = int(input("Input nap time: "))
# ? snooze_time = int(input("Input snooze time: "))
# ? print("Nap time starts.")
# ? printSleepTime(1,nap_time)
# ? x = input("Alarm rings. Dismiss or Snooze: ")
# ? nap_time +=1
# ? while x != 'Dismiss':
# ?         printSleepTime(nap_time,snooze_time)
# ?         x = input("Alarm rings. Dismiss or Snooze: ")
# ?         nap_time += snooze_time

def listFactors(n):
    """
    Get string of factors of n
    :params n is an integer to find factors
    :return string of factors (with a space between each factor)
    >>> listFactors(6)
    '1 2 3 6 '
    >>> listFactors(7)
    '1 7 '
    >>> listFactors(12)
    '1 2 3 4 6 12 '
    """
    string =""
    for i in range(1,n+1):
        if n% i == 0 :
            string += f'{i} '
    return string

def findSumAndNumFactors(n):
    """
    Find summation and count number of factors of n
    :params n is an integer to find factors
    :return sum is summation of factors of n
            count is number of factors of n
    >>> findSumAndNumFactors(6)
    (12, 4)
    >>> findSumAndNumFactors(7)
    (8, 2)
    >>> findSumAndNumFactors(12)
    (28, 6)
    """
    sum_ = 0
    count_ = 0
    factor = listFactors(n)
    listf = factor.split()
    for i in listf:
            count_+=1
            sum_ += int(i)
    return sum_ , count_

# n = int(input("Please input N : "))
# while n >0 :    
#     print(f"Factor of {n} : {listFactors(n)}")
#     x,y = findSumAndNumFactors(n)
#     print(f"Summation of factors is {x}")
#     n = int(input("Please input N : "))
# print("Program End.")

def factorial(x):
    sum = 1
    for i in range(1,x+1):
        sum = i*sum
    return sum

# k = int(input("Input k: "))
# sumfac = 0
# for i in range(1,k):
#     fac = factorial(i)    
#     sumfac += fac
#     print(f"{i}! = {fac}")
# print(f"Summation of factorial 1!-{k}! = {sumfac}")


def getDistance(xPos,yPos):
    """
    Compute distance between origin and (xPos,yPos)
    :params xPos is x-position
            yPos is y-position
    :return distance between origin and (xPos,yPos)
    >>> getDistance(1,1)
    1.4142135623730951
    >>> getDistance(3,4)
    5.0
    >>> getDistance(2,3)
    3.605551275463989
    """
    return (xPos**2 + yPos**2)**0.5

def updatePosition(dir,dist,xPos,yPos):
    """
    Update current position
    :params dir is direction of current move
            dist is distance of current move
    :return xPos is x-position after current move
            yPos is y-position after current move
    >>> updatePosition('N',1.0,0,0)
    (0.0, 1.0)
    >>> updatePosition('NE',1.0,0,0)
    (0.7071067811865475, 0.7071067811865475)
    >>> updatePosition('SW',2.0,1,0)
    (-0.4142135623730949, -1.414213562373095)
    """
    if dir == 'N':
        yPos+= dist
    elif dir == 'E':
        xPos += dist
    elif dir == 'S' :
        yPos -= dist
    elif dir == 'W':
        xPos -= dist
    return xPos,yPos

direction = input("Enter direction : ")
xPos , yPos = 0,0
while direction != 'END' :
    distance = float(input("Enter distance : "))
    xPos,yPos = updatePosition(direction,distance,xPos,yPos)
    direction = input("Enter direction : ")

print(f"Location of treasure is [{xPos:.3f},{yPos:.3f}]")
total_distance = getDistance(xPos,yPos)
print(f"Distance from origin is {total_distance:.3f}")