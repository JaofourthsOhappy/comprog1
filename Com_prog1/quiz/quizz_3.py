import math
def check_unit (unit):

    """Check plural (square meter or square meters)"""
        
    if 0<= unit<=1 :
        return 'square meter.'
    else :
        return 'square meters.'

def cal_circle (radius):

    """Calculate and return area result)"""
        
    area = math.pi *(radius**2)
    return area

def cal_triangle (b,h):

    """Calculate and return area result)"""
        
    area = 0.5*b*h
    return area

def cal_rectangle (w,h):

    """Calculate and return area result)"""
       
    area = w*h
    return area

def print_result (a,name,unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {name} is {a:.2f} {unit}')
# def check_float_input(number):
#     while i = True :

x = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
run = 0
while run ==0 :
    if x  == 'c' or x == 'C':
            r = float(input("Radius = "))
            print('')
            area = cal_circle(r)
            print_result(area,'circle',check_unit(area))
            print('')
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    elif x == 't' or x == 'T':
            base = float(input("base = "))
            print('')
            height=float(input("height = "))
            area = cal_triangle(base,height)
            print_result(area,'triangle',check_unit(area)) 
            print('')
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    elif  x == 'r' or x == 'R':
            width = float(input("width = "))
            height = float(input("height = "))
            area = cal_rectangle(width,height)
            print_result(area,'rectangle',check_unit(area))
            print('')
            x = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    elif x == 'q' or x == 'Q':
        print('Bye')
        run = 1
    else:
        print('Incorrect Input')
     
        x = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
        print('')