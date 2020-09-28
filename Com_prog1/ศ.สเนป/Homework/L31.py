# Level 3


def string_interleave(s1, s2):
    """Start with the first character from the larger of the two strings s1 and s2, take each character from the smaller string from index 0 on and interleave it with each character from the larger string. Return the new interleaved string.

    >>> string_interleave("abc", "mnopq")
    'manbocpq'
    >>> string_interleave("mnopq", "abc")
    'manbocpq'
    >>> string_interleave("Hello", "Sawasdee Thailand")
    'SHaewlalsodee Thailand'
    >>> string_interleave("Mine", "Thai")
    'TMhianie'
    """
    if len(s1) > len(s2):
        base_string = s1
        second_string = s2
    else:
        base_string = s2
        second_string = s1
    index = 0
    interleaved_string = ""
    for char in base_string:
        interleaved_string += char
        if index < len(second_string):
            interleaved_string += second_string[index]
        index += 1
    return interleaved_string


def digit_interleave(n1, n2):
    """Same as string interleave above but treat each digit as character.
    * Hint: you can be smart here by utilizing string_interleave you did previously. *

    >>> digit_interleave(222, 333)
    323232
    >>> digit_interleave(135789, 246)
    123456789
    >>> digit_interleave(246, 135789)
    123456789
    """
    s1 = str(n1)
    s2 = str(n2)
    s3 = string_interleave(s1, s2)
    return int(s3)


def list_union(l1, l2):
    """Given that l1 and l2 are lists containing non-duplicating elements, return the union of l1 and l2.

    >>> list_union([1, 2, 3, 4], [1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> list_union([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> list_union([9, 10, 11, 12], [5, 6, 7, 8])
    [9, 10, 11, 12, 5, 6, 7, 8]
    >>> list_union([9, 10, 11, 12], [5, 6, 9, 10, 7, 8])
    [9, 10, 11, 12, 5, 6, 7, 8]
    """

    combined_list = l1 + l2
    union_list = []
    for element in combined_list:
        if not (element in union_list):
            union_list.append(element)
    return union_list


def list_intersect(l1, l2):
    """Given that l1 and l2 are lists containing non-duplicating elements, return the intersection of l1 and l2.

    >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4]
    >>> list_intersect([9, 10, 11, 12], [5, 6, 7, 8])
    []
    >>> list_intersect([9, 10, 11, 12], [5, 6, 9, 10, 7, 8])
    [9, 10]
    """

    intersect_list = []
    for element in l1:
        if element in l2:
            intersect_list.append(element)
    return intersect_list


def list_difference(l1, l2):
    """Given that l1 and l2 are lists containing non-duplicating elements, return the difference l1 - l2 (elements in l1 that are not in l2).

    >>> list_difference([1, 2, 3, 4], [1, 2, 3, 4])
    []
    >>> list_difference([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4])
    [5, 6, 7, 8]
    >>> list_difference([9, 10, 11, 12], [5, 6, 7, 8])
    [9, 10, 11, 12]
    >>> list_difference([9, 10, 11, 12], [5, 6, 9, 10, 7, 8])
    [11, 12]
    """
    intersect_list = list_intersect(l1, l2)
    diff_list = []
    for element in l1:
        if not (element in intersect_list):
            diff_list.append(element)
    return diff_list
