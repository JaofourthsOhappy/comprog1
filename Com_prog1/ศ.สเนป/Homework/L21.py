# Level 2

def sum_minus_digits(n):
    """Sum all the digits of n starting from right to left. The first digit gets a plus sign, the second digit gest a minus sign, the third digit gets a plus sign, and so on. The alternating between plus and minus sign goes on until the end (leftmost) digit is reached. Return the resulting sum.

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
    sign = 1
    while n > 0:
        rem_digit = n % 10
        sum += sign*rem_digit
        sign = -1*sign
        n = n // 10
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

    # make a list of numbers from the input integer, n, then sort it, and sum the last k values
    number_list = []
    while n > 0:
        rem_digit = n % 10
        number_list.append(rem_digit)
        n = n // 10
    number_list.sort()
    return sum(number_list[-1*k:])

def triple_digits(n):
    """Given a positive integer n, returns a number with each digit tripled.

    >>> triple_digits(1234)
    111222333444
    >>> triple_digits(89643)
    888999666444333
    """
    sum = 0
    mult_factor = 1
    while n > 0:
        rem_digit = n % 10
        sum += rem_digit * mult_factor
        mult_factor = mult_factor * 10
        sum += rem_digit * mult_factor
        mult_factor = mult_factor * 10
        sum += rem_digit * mult_factor
        mult_factor = mult_factor * 10
        n = n // 10
    return sum
