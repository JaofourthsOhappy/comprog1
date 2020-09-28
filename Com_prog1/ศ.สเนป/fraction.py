def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def reduce(m):
    g = gcd(m[0], m[1])
    return [m[0]//g, m[1]//g]

def add(m, n):
    if m[1] == 0 or n[1] == 0:
        raise ZeroDivisionError
    num = m[0]*n[1] + n[0]*m[1]
    den = m[1]*n[1]
    return reduce([num, den])

def negate(m):
    return [-m[0], m[1]]

def subtract(m, n):
    return add(m, negate(n))

def multiply(m, n):
    num = m[0]*n[0]
    den = m[1]*n[1]
    return reduce([num, den])

def fstring(m):
    return str(m[0]) + "/" + str(m[1])