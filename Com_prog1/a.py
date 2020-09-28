import random


def main():
    """This program gives you random integers within the specified range.

    Examples: (uncomment it to test)
        # >>> main()
        # Enter the range of integers you want (a<space>b):
        # >? 1 10
        # Enter the amount of numbers you want:
        # >? 3
        # Here are the random numbers: 3, 10, 2

    <Spoiler Alert> This will *NOT* work because that is simply not how
    doctest works. Doctests DO NOT automate keyboard `input`. Doctest simply
    reads the above text as:
    ``Oh, I should call `main`, then after doing everything it requires, I
    should get the following lines.``

    And those lines would be:
    ``
    Enter the range of integers you want (a<space>b):
    >? 1 10
    Enter the amount of numbers you want:
    >? 3
    Here are the random numbers: 8, 5, 6
    ``

    And that is probably not what you are looking for.
    (You can confirm what I said by running the test in the verbose mode,
    though you will have to be able to exit the program first.)


    What COULD work looks more like this: (uncomment it to test)
        # >>> import random
        # >>> random.seed(1)
        # >>> main()
        # Enter the range of integers you want (a<space>b): Enter the amount of numbers you want: Here are the random numbers: 3, 10, 2

    But you would have to manually type in: ``1<space>10<newline>3`` in the
    console, BLINDLY. Because doctest simply will not print out the `prompt`
    or any output (or any expected input) for you; it is catching output to
    the console to test and see if it matches what you want or not.

    Manually typing something every time we run the file--
    We don't do that here.

    Doctest is meant to be an AUTOMATED test, not a manual test.

    You can try commenting out the first test case and running the doctest
    to confirm what I said. I have already imported doctest for you so you
    can simply run this file.

    (If you pass the test you won't see any further output because that's
    normally what people want for doctests. If you want to see what is
    tested, without failing it, you can run the file like so:
    `python a.py -v`)
    (Of course change python to python3 or whatever you need to)


    Now, if you still aren't giving up on testing user input..
    This is what kind of works: (uncomment it to test)
        # >>> import sys
        # >>> import io
        # >>> import random
        # >>> random.seed(1)
        # >>> sys.stdin = io.StringIO('1 10\\n3\\n')
        # >>> main()
        # Enter the range of integers you want (a<space>b): Enter the amount of numbers you want: Here are the random numbers: 3, 10, 2

    Without going into much detail, all output (excluding what you typed in)
    you see in the console is what is called the `stdout` (standard output),
    which is a ``stream`` that the program gives to the OS (Operating System)
    to print out. The input you type in is similarly called the `stdin`
    (standard input). If you wrote C/C++ before you might be familiar with
    these terms (along with stderr). They are the same thing.

    What I did there was replace the actual stdin stream into a false one
    with the input to be tested already in there. Note the ``\\n``: that is
    how you escape characters in doctests as you have to escape the backlash
    as well (because doctest = docstring = actually a string).

    Since we replaced the actual stdin into a fake one, we have to replace
    it back as well. Else, if you call `input` one more time, you'll have an
    EOF error, because you have already reached the end of the stream.

    I'm not going to tell you how to do that (but it's fairly easy) because
    THERE IS SIMPLY NO NEED FOR ALL THIS COMPLICATIONS.


     Now, on to the way I said you should do: Refactor your code to make it
     easily testable:

     Separate user input and do not test that. Instead, test the other parts
     of your code that is testable. In this case it is whether or not the
     random numbers are of the correct amount, and in the correct range. The
     output can also be tested to see if it is in the correct format.

     You can look at `b.py`.

     /* Personal? Note:
      * This demo program is a bit hard to test (because it involves mostly
      * random processes and user input), but in the end we made some tests.
      * The rock-paper-scissors variant games you need to make is already
      * separated into the right functions that can be tested. Do use it if
      * you cannot think of a way to actually test. (And I mean actually,
      * not what I showed you above-- tests should not come from your
      * program's result, yet that is what I did. I ran the program to see
      * what the output would be with random.seed(1) for a particular input:
      * 1 10\n3. In reality, tests should be written before the code is, as
      * it should be what defines the behaviour of the function/etc, so if
      * you cannot know what a function call should result in (because it's
      * random), you shouldn't test that, because you wouldn't know what
      * behaviour it should have. **Confirming the output is not testing.**
      *
      * Last words:
      * In reality, doctest is mostly use to document the code and serve as
      * examples, so I can see why you might not want to actually test your
      * code, but that doesn't mean you cannot use it to test your code.
      * Even though I know of a better (and the accepted) way to test (using
      * the unittest module), I still use doctest as actual tests for my
      * functions when writing it, as it's really easy to use, and there's
      * no reason to complicate things more that it should, as is the case
      * with our current refactoring-your-code-to-be-testable vs. write-
      * complicated-scripts-to-test-but-not-actually-testing-anything.
      *
      * Side Note: Docstring = description; doctest = >>> thingies
      */
    """
    # *** GET USER INPUT ***
    # get range [a, b]
    valid = False
    while not valid:
        input_str = input("Enter the range of integers you want (a<space>b): ")
        try:
            a, b = input_str.split(' ')
            try:
                a, b = int(a), int(b)
                valid = True
            except ValueError:
                print('Wrong format')  # input is not an integer
        except ValueError:
            print('Wrong format')  # input is not in the correct form
    # get number of output
    n = None
    while n is None:
        input_str = input("Enter the amount of numbers you want: ")
        try:
            n = int(input_str)
        except ValueError:
            print('Wrong format')  # input is not an integer

    # *** GET RANDOM NUMBERS IN THE RANGE [a, b] ***
    # make sure a <= b
    if a > b:
        a, b = b, a
    # get `n` random numbers
    random_nums = []
    for i in range(n):
        # iterate `n` times
        random_nums.append(random.randint(a, b))

    # ***OUTPUT THE RESULT***
    print('Here are the random numbers: ' + ', '.join(map(str, random_nums)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # main()
