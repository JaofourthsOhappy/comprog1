"""
Instruction:
Complete the "YOUR CODE HERE" portion and add two more meaningful testcases to each of the function's doctests.

To test these functions, use the following command:

python3 -m doctest lab3.py
"""
import math

def sum_digits(n):
    """Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> sum_digits(231345)
    18
    >>> sum_digits(75812569)
    43
    """
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    n = str(n)
    if "88" in  n:
        return True
    else :
        return False



def a_plus_abs_b_try(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b_try(2, 3)
    5
    >>> a_plus_abs_b_try(2, -3)
    5
    >>> a_plus_abs_b_try(2, -7)
    9
    >>> a_plus_abs_b_try(2, -7)
    9
    >>> a_plus_abs_b_try(7,-17)
    24
    """
    if b < 0:
        f = a + (0-b)
    else:
        f = a + b
    return f

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> two_of_three(7,2,9)
    130
    """
    if a < b and a< c :
        return b**2 + c**2 
    elif b < a and b <c :
        return a**2 + c**2
    else :
        return b**2 + a**2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    >>> largest_factor(97)
    1
    >>> largest_factor(2019)
    673
    """
    i = 1 
    count = 0
    for i in range(1,n):
        if n% i == 0:
            count = i
    return count

"""
1. Pick a positive integer n as the start.
2. If n is even, divide it by 2.
3. If n is odd, multiply it by 3 and add 1.
4. Continue this process until n is 1.

The number n will travel up and down but eventually end at 1. This sequence of values of n is often called a Hailstone sequence, Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
"""
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> a = hailstone(21)
    21
    64
    32
    16
    8
    4
    2
    1
    >>> print(a)
    8
    >>> a = hailstone(8)
    8
    4
    2
    1
    >>> print(a)
    4
    >>> a = hailstone(17)
    17
    52
    26
    13
    40
    20
    10
    5
    16
    8
    4
    2
    1
    >>> print(a)
    13
    >>> a = hailstone(25)
    25
    76
    38
    19
    58
    29
    88
    44
    22
    11
    34
    17
    52
    26
    13
    40
    20
    10
    5
    16
    8
    4
    2
    1
    >>> print(a)
    24
    """
    i = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = (n * 3) + 1
        i += 1
    print(n)
    return i

"""
For the following problems, you have to write at least 5 testcases of your own.
"""

def is_leap_year(year):
    """Return True if year is a leap year, otherwise return False.
    >>> is_leap_year(2548)
    True
    >>> is_leap_year(1998)
    False
    >>> is_leap_year(1669)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2000)
    True
    """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else :
        return False

def interval_intersect(a, b, c, d):
    """Return True if the intervals [a,b] and [c,d] intersect and False otherwise.
    >>> interval_intersect(1,5,2,7)
    True
    >>> interval_intersect(1,2,1,2)
    True
    >>> interval_intersect(5,9,15,17)
    False
    >>> interval_intersect(2,4,7,9)
    False
    >>> interval_intersect(12,14,16,18)
    False
    """
    AB = set(range(a,b+1))
    CD = set(range(c,d+1))
    if len(AB.intersection(CD)) != 0 :
        return True
    else :
        return False

def smaller_root(a, b, c):
    """Returns the smaller root of a quadratic equation a*x^2 + b*x + c = 0 if one exists. If
    the equation has no real solution, print the message "Error: No real solutions" and simply return.

    >>> smaller_root(7,2,4)
    Error: No real solutions
    >>> smaller_root(1,2,1)
    -1.0
    >>> smaller_root(1,6,7)
    (-1.5857864376269049, -4.414213562373095)
    >>> smaller_root(2,14,2)
    (-0.1458980337503153, -6.854101966249685)
    >>> smaller_root(4,7,12)
    Error: No real solutions

    """
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()