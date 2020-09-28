# Level 1

def all_equal_int(x1, x2, x3, x4):
    """Return True if all input integers, x1, x2, x3, and x4 are equal

    >>> all_equal_int(3, 3, 3, 3)
    True

    >>> all_equal_int(3, 2, 2, 3)
    False

    >>> all_equal_int(3, 2, 2, 2)
    False

    >>> all_equal_int(3, 3, 3, 2)
    False

    """
    list = [x1,x2,x3,x4]
    count =0 
    use = []
    step =1
    for i in list :
        # use.append(i)
        # if i in use :
        #     count += 1
        if i == list[step]:
            count +=1
    if count == len(list):
        return True
    else:
        return False

def circles_overlapping(x1, y1, x2, y2, r):
    """Return True if two circles with the same radius, r, located at (x1, y1) and (x2, y2) overlapped; return False, otherwise

    >>> circles_overlapping(0, 0, 2, 0, 2)
    True

    >>> circles_overlapping(2, 2, 4, 2, 0.7)
    False

    >>> circles_overlapping(1, 1, 2, 2, 0.6)
    False

    >>> circles_overlapping(1, 1, 4, 5, 3)
    True

    """
    difx = x2-x1 
    dify =y2-y1
    pita = (difx**2 + dify**2)**0.5
    if pita <(2*r):
        return True
    else :
        return False
