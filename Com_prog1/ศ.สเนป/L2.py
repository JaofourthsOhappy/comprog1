# Level 2

def sum_minus_digits(n):
    """Sum all the digits of n starting from right to left. The first digit gets a plus sign, the second digit gest a minus sign, the third digit gets a plus sign, and so on. 
    The alternating between plus and minus sign goes on until the end (leftmost) digit is reached. Return the resulting sum.

    >>> sum_minus_digits(10) # 0 - 1 = -1
    -1
    >>> sum_minus_digits(4224) # 4 - 2 + 2 - 4 = 0
    0
    >>> sum_minus_digits(1234567890) # 0 - 9 + 8 - 7 + 6 - 5 + 4 - 3 + 2 - 1
    -5
    >>> sum_minus_digits(10101010) # 0 - 1 + 0 - 1 + 0 - 1 + 0 - 1
    -4
    """
    sum = 0
    n = str(n)[::-1]
    k = 0
    for i in n:        
        k += 1
        sign = (-1)**(k+1)
        sum  += (sign* int(i))
    return sum

def selective_sum(n, k):
    """Return the sum of the k largest digits of n.

    >>> selective_sum(3018, 2) # 3 and 8 are the 2 largest digits (larger than 0 and 1).
    11
    >>> selective_sum(593796, 3) # 9, 9, and 7 are the 3 largest digits.
    25
    >>> selective_sum(12345, 10) # Sum all the digits since k is larger than the number of digits in n
    15
    """
    n = str(n)
    sum =0
    count = 0
    for i in (sorted(n)[::-1]):
        count += 1
        if count <= k :
            sum += int(i)
        else:
            break
    return sum
def triple_digits(n):
    """Given a positive integer n, returns a number with each digit tripled.

    >>> triple_digits(1234)
    111222333444
    >>> triple_digits(89643)
    888999666444333
    """
    n= str(n)
    string = ''
    for i in n :
        string += i*3
    return int(string)