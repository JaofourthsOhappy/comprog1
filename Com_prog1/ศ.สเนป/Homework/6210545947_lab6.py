#No1
def ll_sum(t):
    """
    >>> t = [[1],[2,3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> t = [[-2],[],[7,6,5]]
    >>> ll_sum(t)
    16
    >>> t = [[-5,-4],[0],[4,5]]
    >>> ll_sum(t)
    0
    >>> t = [[0,0],[0],[0,0,0]]
    >>> ll_sum(t)
    0
    >>> t = [[-54,-5],[93,4],[-45]]
    >>> ll_sum(t)
    -7
    """
    sum = 0
    for ele in t:
        for x in ele:
            sum = sum+x
    return sum

#No.2
def cumulative_sum(t):
    """
    >>> t = [1,4,5,3]
    >>> cumulative_sum(t)
    [1, 5, 10, 13]
    >>> t = [0,0,0]
    >>> cumulative_sum(t)
    [0, 0, 0]
    >>> t = [-5,-4]
    >>> cumulative_sum(t)
    [-5, -9]
    >>> t = [4,-5,6,-7,9]
    >>> cumulative_sum(t)
    [4, -1, 5, -2, 7]
    >>> t = [4,52,4,3,-100]
    >>> cumulative_sum(t)
    [4, 56, 60, 63, -37]
    """
    c = []
    sum = 0
    for ele in t:
        sum = ele + sum
        c.append(sum)
    return c
#No.3
def middle(t):
    """
    >>> t = [1,2,5,6,77,7,7]
    >>> middle(t)
    [2, 5, 6, 77, 7]
    >>> t=[1,[2],[3,4],5]
    >>> middle(t)
    [[2], [3, 4]]
    >>> t = [2,4,5]
    >>> middle(t)
    [4]
    >>> t =[3.4]
    >>> middle(t)
    []
    >>> t = [3,4,5,6,7,8]
    >>> middle(t)
    [4, 5, 6, 7]
    """
    x = []
    for i in t[1:-1]:
        x.append(i)
    return x

#No.4
def chop (t):
     """
    >>> t = [1,2,5,6,77,7,7]
    >>> chop(t)

    >>> t
    [2, 5, 6, 77, 7]
    >>> t = [1,[2],[3,4],5]
    >>> chop(t)

    >>> t
    [[2], [3, 4]]
    >>> t = [2,4,5]
    >>> chop(t)

    >>> t
    [4]
    >>> t =[3,4]
    >>> chop(t)

    >>> t
    []
    >>> t = [3,4,5,6,7,8]
    >>> chop(t)

    >>> t
    [4, 5, 6, 7]
    """
     t.pop(0)
     t.pop(-1)
     
#No.5
def is_sorted(t):
    """
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['z','a'])
    False
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted(['abc','bcd','cdf'])
    True
    """
    if t == sorted(t):
        return True
    else:
        return False
#No.6
def front_x(lists):
    """
    >>> lists = ['iwe','ert','xxxx','tgb,']
    >>> front_x(lists)
    ['xxxx', 'ert', 'iwe', 'tgb,']
    >>> lists = ['porn','apps']
    >>> front_x(lists)
    ['apps', 'porn']
    >>> lists = ['xavier','xiao','xin']
    >>> front_x(lists)
    ['xavier', 'xiao', 'xin']
    >>> lists = ['olo','kuy','joo','xuy']
    >>> front_x(lists)
    ['xuy', 'joo', 'kuy', 'olo']
    >>> lists = ['yui','mio','koi','mao']
    >>> front_x(lists)
    ['koi', 'mao', 'mio', 'yui']
    """
    lists.sort()
    a = []
    b = []
    for i in lists :
        if i[0] == 'x':
            a.append(i)
        else:
            b.append(i)  
    return a+b

#No.7
def even_only(t):
    """
    >>> even_only([1,3,4,5,67,7,8])
    [4, 8]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([3,4,5,0])
    [4, 0]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([3,5,6,8,0])
    [6, 8, 0]
    """
    l = []
    for ele in t :
        if ele %2 == 0:
            l.append(ele)
        else:
            pass
    return l
#No.8
def love(text):
    """
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love('I hate you')
    'I love you'
    >>> love('I do not like you')
    'I do not love you'
    >>> love('He would like to fuck up')
    'He would like to love up'
    """
    x = text.split(' ')
    x[-2] = 'love'
    return (' ' .join(x))
#No.9
def is_anagram(string1,string2):
    """
    >>> is_anagram('arrange', 'rearnag')
    True
    >>> is_anagram('power','owerp')
    True
    >>> is_anagram('poer','roerr')
    False
    >>> is_anagram('work hard','dworka har')
    False
    >>> is_anagram('kaopun','apounk')
    True
    """

    if sorted(string1) ==  sorted(string2):
        return True
    else :
        return False
#No.10
def has_duplicate(l):
    """
    >>> has_duplicate([1,2,3,4,5])
    False
    >>> has_duplicate([1,2,3,2,3])
    True
    >>> has_duplicate([1,1,1,3,4])
    True
    >>> has_duplicate([3,4,7,5,7])
    True
    >>> has_duplicate([0,0,0,0,0,0,0])
    True
    """
    dup = []
    for i in l:
        if i not in dup:
            dup.append(i)
    if len(dup) < len(l) :
        return True
    else:
        return False
#No.11
def average(l):
    """
    >>> average([1,2,3,4,5])
    3.0
    >>> average([1,2,3,2,3])
    2.2
    >>> average([1,1,1,3,4])
    2.0
    >>> average([3,4,7,5,7])
    5.2
    >>> average([0,0,0,0,0,0,0])
    0.0
    """
    x= sum(l)/len(l)
    return x
def centered_average(l):
    """
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([1,2,3,7,3])
    4.0
    >>> centered_average([1,1,0,5,4])
    2.0
    >>> centered_average([3,4,5,6,7])
    5.0
    >>> centered_average([0,0,0,0,0,0,0])
    0.0
    """
    x = sum(l[1:-1])/(len(l[1:-1]))
    return x
#No.13
def reverse_pair(s):
    """
    >>> reverse_pair("I like Python")
    'Python like I'
    >>> reverse_pair("I really like Python")
    'Python like really I'
    >>> reverse_pair('I hate you')
    'you hate I'
    >>> reverse_pair('I do not like you')
    'you like not do I'
    >>> reverse_pair('He would like to fuck up')
    'up fuck to like would He'
    """
    x = s.split(' ')
    w=x[::-1]
    return (' '.join(w))
#No.14
def match_ends(l):
    """
    >>> match_ends(["olo",'hello',"oreo"])
    2
    >>> match_ends(["lul",'ooo','ad'])
    2
    >>> match_ends(['efad','dsaf','sadf'])
    0
    >>> match_ends(['qweq','ikv'])
    1
    >>> match_ends(['aug','mum','o'])
    1
    """
    count =0
    for i in l :
        if len(i) >= 2 and (i[0] == i[-1]):
            count+=1
    return count
#No.15
def remove_adjacent(l):
    """
    >>> remove_adjacent([1,3,4,5,6,1])
    [1, 3, 4, 5, 6, 1]
    >>> remove_adjacent([2,4,4,4,5,6])
    [2, 4, 5, 6]
    >>> remove_adjacent([3,-4,-3,-5,0])
    [3, -4, -3, -5, 0]
    >>> remove_adjacent([0,0,0,0,0])
    [0]
    >>> remove_adjacent([1,1,3,1,1,6,7])
    [1, 3, 1, 6, 7]
    """
    i =1
    while i < len(l):
        if l[i] == l[i-1]:
            l.pop(i)
            i -= 1 
        i += 1
    return l
