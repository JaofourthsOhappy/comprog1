"""
Instruction:
Complete the "YOUR CODE HERE" portion and add two more meaningful testcases to each of the function's doctests.

To test these functions, use the following command:

python3 -m doctest lab3.py
"""

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "code"
    
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
    "*** YOUR CODE HERE ***"
    n = str(n)
    if '88' in n :
        return True  
    else:
        return False

def a_plus_abs_b_try(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b_try(2, 3)
    5
    >>> a_plus_abs_b_try(2, -3)
    5
    """
    if b < 0:
        f = a+(b*(-1))
    else:
        f = a+b
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
    """
    if a<b and a<c :
        return b**2+ c**2
    elif b<c and b<a :
        return c**2 + a**2
    else :
        return a**2 + b**2

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i =1
    while i <= n :
        if n% i == 0:
            i = i+1
    return i

# """
# 1. Pick a positive integer n as the start.
# 2. If n is even, divide it by 2.
# 3. If n is odd, multiply it by 3 and add 1.
# 4. Continue this process until n is 1.

# The number n will travel up and down but eventually end at 1. This sequence of values of n is often called a Hailstone sequence, Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
# """
# def hailstone(n):
#     """Print the hailstone sequence starting at n and return its
#     length.

#     >>> a = hailstone(10)
#     10
#     5
#     16
#     8
#     4
#     2
#     1
#     >>> a
#     7
#     """
#     "*** YOUR CODE HERE ***"

# """
# For the following problems, you have to write at least 5 testcases of your own.
# """

def is_leap_year(year):
    """Return True if year is a leap year, otherwise return False.

    *** YOUR DOCTESTS HERE ***
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(1904)
    True
    >>> is_leap_year(1864)
    True
    >>> is_leap_year(1505)
    False
    >>> is_leap_year(14050)
    False
    """
    "*** YOUR CODE HERE ***"
    if (year % 4) !=0 :
        return False
    elif (year % 100 ) != 0 :
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

def interval_intersect(a, b, c, d):
    """Return True if the intervals [a,b] and [c,d] intersect and False otherwise.

        *** YOUR DOCTESTS HERE ***


    """
    "*** YOUR CODE HERE ***"

# def smaller_root(a, b, c):
#     """Returns the smaller root of a quadratic equation a*x^2 + b*x + c = 0 if one exists. If
#     the equation has no real solution, print the message "Error: No real solutions" and simply return.

#         *** YOUR DOCTESTS HERE ***


#     """
#     "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
