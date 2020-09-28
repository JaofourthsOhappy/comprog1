import math
def check_unit (unit):     
    if 0<= unit<=1 :
        return 'square meter.'
    else :
        return 'square meters.'

def cal_circle (radius):       
    area = math.pi *(radius**2)
    return area

def cal_triangle (b,h):       
    area = 0.5*b*h
    return area

def cal_rectangle (w,h):  
    area = w*h
    return area

def print_result (a,name,unit):

    print(f'Area of this {name} is {a:.2f} {unit}')

menu = input("(T)riangle (R)ectangle (C)ircle : ")
if menu == 't' or menu == 'T':
    base = float(input("base = "))
    height=float(input("height = "))
    area = cal_triangle(base,height)
    print_result(area,'triangle',check_unit(area))
elif menu == 'c' or menu == 'C':
    r = float(input("Radius = "))
    area = cal_circle(r)
    print_result(area,'circle',check_unit(area))
elif menu == 'r' or menu == 'R':
    width = float(input("width = "))
    height = float(input("height = "))
    area = cal_rectangle(width,height)
    print_result(area,'rectangle',check_unit(area))
else:
    print("Incorrect Input!")

