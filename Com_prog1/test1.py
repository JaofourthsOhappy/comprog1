# """
#     >>> sum_minus_digits(10) # 0 - 1 = -1
#     -1
#     >>> sum_minus_digits(4224) # 4 - 2 + 2 - 4 = 0
#     0
#     >>> sum_minus_digits(1234567890) # 0 - 9 + 8 - 7 + 6 - 5 + 4 - 3 + 2 - 1
#     -5
#     >>> sum_minus_digits(10101010) # 0 - 1 + 0 - 1 + 0 - 1 + 0 - 1
#     -4
# """
# n = 4224
# sum = 0
# n = str(n)[::-1]
# print(n)
# k = 0
# for i in n:        
#     k += 1
#     sign = (-1)**(k+1)
#     sum  += (sign* int(i))
# print(sum)    
"""Return the sum of the k largest digits of n.

    >>> selective_sum(3018, 2) # 3 and 8 are the 2 largest digits (larger than 0 and 1).
    11
    >>> selective_sum(593796, 3) # 9, 9, and 7 are the 3 largest digits.
    25
    >>> selective_sum(12345, 10) # Sum all the digits since k is larger than the number of digits in n
    15
"""
# n =3018
# k = 2
# n = str(n)
# sum =0
# count = 0
# for i in (sorted(n)[::-1]):
#     count += 1
#     if count <= k :
#         sum += int(i)
#     else:
#         break
# print(sum)
"""
    >>> string_interleave("abc", "mnopq")
    'manbocpq'
    >>> string_interleave("mnopq", "abc")
    'manbocpq'
    >>> string_interleave("Hello", "Sawasdee Thailand")
    'SHaewlalsodee Thailand'
    >>> string_interleave("Mine", "Thai")
    'TMhianie'
"""
a = []
s1 = 'Hello'
s2 = 'Sawasdee Thailand'
if s1 > s2:
    first = s1
    second = s2
elif s2>s1 :
    first = s2
    second = s1
k = 0
for i in first:
    a.append(i)
    if k < len(second):
        a.append(second[k])
        k+=1
        

print("".join(a))

