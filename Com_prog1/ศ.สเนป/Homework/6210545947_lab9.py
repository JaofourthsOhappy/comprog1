#No.1
def n_dict(n):
    """
    to generate and print a dictionary that contains a number 
    (between 1 and n) in the form (x, x*x).
    >>> n_dict(1)
    {1: 1}
    >>> n_dict(2)
    {1: 1, 2: 4}
    >>> n_dict(3)
    {1: 1, 2: 4, 3: 9}
    >>> n_dict(4)
    {1: 1, 2: 4, 3: 9, 4: 16}
    >>> n_dict(0)
    {}
    """
    d = dict()
    val = d.values()
    for i in range(n):
        d[i+1] = (i+1)**2
    return d

#N0.2
def dict_from_2list(list1,list2):
    """
    >>> keys = ['red', 'green', 'blue']
    >>> values = ['#FF0000','#008000', '#0000FF']
    >>> dict_from_2list(keys,values)
    {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
    >>> key = ['1','2','3']
    >>> value = ['one' , 'two' , 'three']
    >>> dict_from_2list(key,value)
    {'1': 'one', '2': 'two', '3': 'three'}
    >>> key = [1, 2, 3, 4]
    >>> value = ['one' , 'two' , 'three' , 'four']
    >>> dict_from_2list(key,value)
    {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    >>> key = ['one' , 'two' , 'three' , 'four']
    >>> value = [1, 2, 3, 4]
    >>> dict_from_2list(key,value)
    {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    >>> key = ['#FF0000','#008000', '#0000FF']
    >>> value = ['red', 'green', 'blue']
    >>> dict_from_2list(key,value)
    {'#FF0000': 'red', '#008000': 'green', '#0000FF': 'blue'}
    """
    d = dict()
    val = d.values()
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

#No.3
def max_min(d):
    """
    >>> my_dict = {'x' :500 , 'y' :5874 , 'z' :560}
    >>> max_min(my_dict)
    Maximum Value: 5874
    Minimum Value: 500
    >>> d = {'a' : 0 , 'b' : 1 , 'c' : 2} 
    >>> max_min(d)
    Maximum Value: 2
    Minimum Value: 0
    >>> d = {'a' : -3 , 'b' : 0 , 'c' : 3}
    >>> max_min(d)
    Maximum Value: 3
    Minimum Value: -3
    >>> d = {1 :20 , 2 :40 , 3 : 50}
    >>> max_min(d)
    Maximum Value: 50
    Minimum Value: 20
    >>> d = {1 :20}
    >>> max_min(d)
    Maximum Value: 20
    Minimum Value: 20
    """
    val = d.values()
    a = []
    for i in val:
        a.append(i)
    print(f"Maximum Value: {max(a)}")
    print(f"Minimum Value: {min(a)}")

#No.4
def combine_dict(d1,d2):
    """
    >>> d1 = {'x' :500 , 'y' :5874 , 'z' :560}
    >>> d2 = {'x' :500 , 'y' :5874 , 'z' :560}
    >>> combine_dict(d1,d2)
    {'x': 1000, 'y': 11748, 'z': 1120}
    >>> d1 = {'a' : 0 , 'b' : 1 , 'c' : 2} 
    >>> d2 = {'a' : 0 , 'b' : 1 , 'c' : 2, 'd' : 4} 
    >>> combine_dict(d1,d2)
    {'a': 0, 'b': 2, 'c': 4, 'd': 4}
    >>> d1 = {'a' : -3 , 'b' : 0 , 'c' : 3}
    >>> d2 = {'x' :500 , 'y' :5874 , 'z' :560}
    >>> combine_dict(d1,d2)
    {'a': -3, 'b': 0, 'c': 3, 'x': 500, 'y': 5874, 'z': 560}
    >>> d1 = {2: 3 , 4: 5 , 6: 7}
    >>> d2 = {4: 6 , 5: 6}
    >>> combine_dict(d1,d2)
    {2: 3, 4: 11, 6: 7, 5: 6}
    >>> d1 = {-1 : 3 , 4: 5 , 7: 3}
    >>> d2 = {}
    >>> combine_dict(d1,d2)
    {-1: 3, 4: 5, 7: 3}
    """
    com_d = {}
    for i in d1:
        if i in d2:
            com_d[i] = d1[i]+ d2[i]
        else:
            com_d[i] = d1[i]
    for i in d2 :
        if i not in com_d:
            com_d[i] = d2[i]
    return com_d
#No.5
def three_highest(d):
    """
    >>> d = {'x' :500 , 'y' :5874 , 'z' :560}
    >>> three_highest(d)
    ['y', 'z', 'x']
    >>> d = {'a' : 500 , 'b' :5874 , 'c' :560 , 'd' :400 , 'e' :5874 , 'f' :20}
    >>> three_highest(d)
    ['b', 'e', 'c']
    >>> d = {'a' : 0 , 'b' : 1 , 'c' : 2} 
    >>> three_highest(d)
    ['c', 'b', 'a']
    >>> d = {-1 : 3 , 4: 5 , 7: 2}
    >>> three_highest(d)
    [4, -1, 7]
    >>> d = {'a' : -3 , 'b' : 0 , 'c' : 3}
    >>> three_highest(d)
    ['c', 'b', 'a']
    """
    return sorted(d, key = d.get , reverse = True) [:3]

#No.6
def count_list(d):
    """
    >>> dict = {'Alex' : ['sub1' ,'sub2' , 'sub3'], 'Tom':2 , 'David' : ['sub1' , 'sub2']}
    >>> count_list(dict)
    5
    >>> dict = {}
    >>> count_list(dict)
    0
    >>> dict = {'o' : [] , 'p' : []}
    >>> count_list(dict)
    0
    >>> dict = {'q' : [1,3,4]}
    >>> count_list(dict)
    3
    >>> dict = {1 : [3] , 2 : 2}
    >>> count_list(dict)
    1
    """
    sum_ = 0
    val = d.values()
    for i in val:
        if type(i) == list:
            sum_ += len(i)
    return sum_