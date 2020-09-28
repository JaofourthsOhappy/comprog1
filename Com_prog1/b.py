import random


def get_two_integers(prompt) -> (int, int):
    """Return two integers"""
    while True:
        input_str = input(prompt)
        try:
            int1, int2 = input_str.split(' ')
            try:
                int1, int2 = int(int1), int(int2)
                return int1, int2
            except ValueError:
                print('Wrong format')  # input is not an integer
        except ValueError:
            print('Wrong format')  # input is not in the correct form


def get_integer(prompt) -> int:
    """Return an integer"""
    while True:
        input_str = input(prompt)
        try:
            int1 = int(input_str)
            return int1
        except ValueError:
            print('Wrong format')  # input is not an integer


def my_randint(a: int, b: int, n: int = 1) -> list:
    """Return `n` random integers in [a, b].

    Examples:
        >>> lst = my_randint(1, 10, 3)
        >>> len(lst)
        3
        >>> 1 <= lst[0] <= 10
        True
        >>> 1 <= lst[1] <= 10
        True
        >>> 1 <= lst[2] <= 10
        True

        # another way for larger `n`
        >>> lst = my_randint(20, 3, 100)
        >>> len(lst)
        100
        >>> def f(elem): return 3 <= elem <= 20
        >>> len(list(filter(None, map(f, lst))))
        100
    """
    # make sure a <= b
    if a > b:
        a, b = b, a
    # get `n` random numbers
    random_nums = []
    for i in range(n):
        # iterate `n` times
        random_nums.append(random.randint(a, b))
    return random_nums


def comma_separated_string(lst: list) -> str:
    """Return a string of comma and space separated value

    Examples:
        >>> comma_separated_string([1, 2, 3, 4])
        '1, 2, 3, 4'
        >>> comma_separated_string([5, 6, 1, 8, 9])
        '5, 6, 1, 8, 9'
        >>> comma_separated_string(['a', 'd', 0, 6])
        'a, d, 0, 6'
    """
    return ', '.join(map(str, lst))


def main():
    """This program gives you random integers within the specified range."""
    # *** GET USER INPUT ***
    # get range [a, b]
    a, b = get_two_integers("Enter the range of integers you want (a<space>b): ")
    # get number of output
    n = get_integer("Enter the amount of numbers you want: ")

    # *** GET RANDOM NUMBERS IN THE RANGE [a, b] & OUTPUT THE RESULT ***
    print('Here are the random numbers: '
          + comma_separated_string(my_randint(a, b, n)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # main()
