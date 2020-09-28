# level1
# import math 
# def define(letter):
#     if letter == 't' or letter == 'T':
#         letter = 'triangle'
#     elif letter == 'r' or letter == 'R' : 
#         letter = 'rectangle'
#     elif letter == 'c' or letter == 'C':
#         letter = 'circle'
#     elif letter == 'q' or letter == 'Q':
#         letter = 'quit'
#     else :
#         letter = False
#     return letter

# def circle():
#     r = float(input("Radius = "))
#     area = math.pi *(r**2)
#     return area

# def triangle():
#     base = float(input("base = "))
#     height=float(input("height = ") )
#     area = 0.5* base * height
#     return area
# def rectangle():
#     width = float(input("width = "))
#     height = float(input("height = "))
#     area = width * height
#     return area

# def plural(area):
#     if 0<= area <=1 :
#         return 'meter.'
#     else :
#         return 'meters'

# x = input("(T)riangle (R)ectangle (C)ircle : ")
# if define(x) == 'circle':
#     area = circle()
#     print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
# elif define(x) == 'triangle':
#     area = triangle()
#     print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
# elif define(x) == 'rectangle' :
#     area = rectangle()
#     print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
# elif define(x) == False :
#     print('Incorrect input!')

#level2
import math 
def define(letter):
    if letter == 't' or letter == 'T':
        letter = 'triangle'
    elif letter == 'r' or letter == 'R' : 
        letter = 'rectangle'
    elif letter == 'c' or letter == 'C':
        letter = 'circle'
    elif letter == 'q' or letter == 'Q':
        letter = 'quit'
    else :
        letter = False
    return letter

def circle():
    r = (input("Radius = "))
    area = math.pi *(r**2)
    return area

def triangle():
    base = float(input("base = "))
    height=float(input("height = ") )
    area = 0.5* base * height
    return area
def rectangle():
    width = float(input("width = "))
    height = float(input("height = "))
    area = width * height
    return area

def plural(area):
    if 0<= area <1 :
        return 'meter.'
    else :
        return 'meters'

x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
run = 0
while run == 0 :
    if define(x) == False :
        print('Incorrect input!')
        x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
    elif define(x) == 'circle':
            area = circle()
            print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
    elif define(x) == 'triangle':
            area = triangle()
            print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
    elif define(x) == 'rectangle' :
            area = rectangle()
            print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
    elif define(x) == 'quit':
        print('Bye')
        run = 1




# #level3
# import math 
# def define(letter):
#     if letter == 't' or letter == 'T':
#         letter = 'triangle'
#     elif letter == 'r' or letter == 'R' : 
#         letter = 'rectangle'
#     elif letter == 'c' or letter == 'C':
#         letter = 'circle'
#     elif letter == 'q' or letter == 'Q':
#         letter = 'quit'
#     else :
#         letter = False
#     return letter

# def circle():
#     r = (input("Radius = "))
#     while check_input(r) == False :
#         r = float(input("Radius = "))
#     r = float(r)
#     area = math.pi *(r**2)
#     return area

# def triangle():
#     base = float(input("base = "))
#     while check_input(base) == False :
#         base =  float(input("base = "))
#     base = float(base)
#     height= float(input("height = "))
#     while check_input(height) == False:
#         height= float(input("height = "))
#     height = float(height)
#     area = 0.5* base * height
#     return area
# def rectangle():
#     width = float(input("width = "))
#     while check_input(width) == False :
#         width = float(input("width = "))
#     width = float(width)
#     height = (input("height = "))
#     while check_input(height) == False:
#         height = (input("height = "))
#     width = float(width)
#     area = width * height
#     return area

# def plural(area):
#     if 0<= area <1 :
#         return 'meter.'
#     else :
#         return 'meters'
# def check_input(value): 
#         if type(value) == float : 
#             return True
#         else:
#             print("Please enter a number!")
#             return False


# x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
# run = 0
# while run == 0 :
#     if define(x) == False :
#         print('Incorrect input!')
#         x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
#     elif define(x) == 'circle':
#             area = circle()
#             print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
#             x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
#     elif define(x) == 'triangle':
#             area = triangle()
#             print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
#             x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
#     elif define(x) == 'rectangle' :
#             area = rectangle()
#             print(f"Area of this {define(x)} is {area:.2f} square {plural(area)}")
#             x = input("(T)riangle (R)ectangle (C)ircle (Q)uit: ")
#     elif define(x) == 'quit':
#         print('Bye')
#         run = 1

