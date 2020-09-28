# Level 1

def interval_contain(a, b, c, d):
    """Return True if the interval [a,b] is within the interval [c,d] and False otherwise.

    >>> interval_contain(2, 7, 3, 4)
    False
    >>> interval_contain(3, 4, 2, 7)
    True
    >>> interval_contain(2, 8, 2, 8)
    True
    >>> interval_contain(2, 7, 1, 9)
    True
    >>> interval_contain(2, 7, 8, 9)
    False
    """
    if a >= c and b <= d :
        return True
    else :        
        return False

def make_triangle(a, b, c):
    """Return 0 if the three lengths a, b, and c do not form a triangle, 1 if they form a right angle triangle, 2 if they form other type of triangle. If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can.

    >>> make_triangle(2, 10, 3)
    0
    >>> make_triangle(5, 12, 13)
    1
    >>> make_triangle(10, 8, 6)
    1
    >>> make_triangle(20, 40, 30)
    2
    >>> make_triangle(88, 12, 76)
    2
    """
    if a == (b**2 + c**2)**0.5 or b == (c**2 + a**2)**0.5 or c == (a**2 + b**2)**0.5 :
        return 1
    elif a+b >=c and  a+c >=b and  b+c >=a:
        return 2
    else: 
        return 0

def print_series(n):
    """print the first nth terms in this serie: 1, 1/3, 1/5, 1/7, 1/9, ... ,1/(2*n + 1)

    >>> print_series(0)
    1
    >>> print_series(1)
    1
    1 / 3
    >>> print_series(4)
    1
    1 / 3
    1 / 5
    1 / 7
    1 / 9
    """
    k =1
    print(k)
    for i in range(1,n+1) :
                k+=2
                print(f'1 / {k}')
                