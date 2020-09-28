# Level 4

def group_elements(l):
    """Return a list of lists where each list groups the same element(s) from the input list, l, together

    >>> group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]

    >>> group_elements([3, 3, 3, 3])
    [[3, 3, 3, 3]]

    >>> group_elements([3, 3, 1, 3, 3, 1])
    [[3, 3, 3, 3], [1, 1]]

    >>> group_elements([5, 3, 1, 2, 4, 10])
    [[5], [3], [1], [2], [4], [10]]

    """
    str = []
    for i in l :
        if i in str :
            str.append(i)
    return ""

def dup_elements(l):
    """Return a list that contains only duplicate elements of the input list, l; use the group_elements to help solve this one

    >>> dup_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [3, 5]

    >>> dup_elements([3, 3, 3, 3])
    [3]

    >>> dup_elements([3, 3, 1, 3, 3, 1])
    [3, 1]

    >>> dup_elements([5, 3, 1, 2, 4, 10])
    []

    """
    l1 =[]
    l2 = []
    for i in l :
        l1.append(i)
        if i in l1 :
            l2.append(i)
    return l2

def count_unique_elements(l):
    """Return the total number of unique elements in the input list, l; use the group_elements to help solve this one

    >>> count_unique_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    6

    >>> count_unique_elements([3, 3, 3, 3])
    0

    >>> count_unique_elements([3, 3, 1, 3, 3, 1])
    0

    >>> count_unique_elements([5, 3, 1, 2, 4, 10])
    6

    """
    str = []
    count = 0
    for i in l:
        str.append(i)
        if not(i in str):
            count+=1
    print(str)
    return count
