def fib(n):
    """This function prints a Fibonacci sequence up to 
    the nth Fibonacci
    """
    list_ = "1 "
    seq = 1
    a = 0
    if n < 2:
        for i in range(n):
            list_+="1 "
    else:
        for i in range(n):
            next_seq = seq +a
            list_+= f"{next_seq} "
            a = seq
            seq = next_seq
    print(list_)
# fill me in
# print("fib(n) result:")
# n = 0
# while n < 10:
#     fib(n)
#     print("")
#     n += 1

def diamond(n):
    """This function prints a diamond shape of size n 
    as shown in loop_exercise_result.txt
    """
    e = 2
    space = ' '
    j = 0
    k = n-1
    for i in range(n):
            print(space*k+"*"*e+space*k)
            e+=2
            k-=1
    f = e
    for i in range(n):
        f -= 2
        print(space*j+"*"*f+space*j)
        j+=1

# fill me in

print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")

def hailstone(n):
    """This function prints a hailstone sequence whose 
    details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html
    """
    string = ""
    i = 1
    while n != 1:
        string+= f"{n} "
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = (n * 3) + 1
        i += 1
    print (string+f"{1}")
# fill me in

# print("hailstone(n) result:")
# for i in range(1, 8):
#     hailstone(i)
#     print("")

def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum
    """

    sum = 0
    count = 1
    string = f"{count} " 
    for i in range(n):
        sum = sum+count
        string+= f"+ {count}  "
        count += 1
    print(f"{string} = {sum}")
# fill me in

print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")  