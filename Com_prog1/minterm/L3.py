# Level 3

def string_union(str1, str2):
    """Return a union of the characters in the two input strings str1 and str2; you can assume that the two strings have no duplicate characters

    >>> string_union("abcde", "abcwxyz")
    'abcdewxyz'

    >>> string_union("abcde", "wxyz")
    'abcdewxyz'

    >>> string_union("abcde", "wxyabzc")
    'abcdewxyz'

    """
    string = [str1]
    for i in str2 :
        if i not in str1:
            string.append(i)    
    return "".join(string)
def string_intersect(str1, str2):
    """Return an intersection of the characters in the two input strings str1 and str2; you can assume that the two strings have no duplicate characters

    >>> string_intersect("abcde", "abcwxyz")
    'abc'

    >>> string_intersect("abcde", "wxyz")
    ''

    >>> string_intersect("abcde", "wxyabzc")
    'abc'

    """
    string = []
    for i in str2:
        if i in str1 :
            string.append(i)
    return "".join(string)
