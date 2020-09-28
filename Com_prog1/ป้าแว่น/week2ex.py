# import math

# def read_two_floats(str1, str2):  
#     x = float(input(str1))
#     y = float(input(str2))
#     return x,y


# def read_three_floats(str1, str2, str3):    
#     x = float(input(str1))
#     y = float(input(str2))
#     z = float(input(str3))
#     return x,y,z
# ####################################################################
# def compute_circle_area(r):
#     return math.pi * (r**2)
# def compute_rectangle_area(w, l):
#     return w*l
# ####################################################################
# def compute_volume(base, h):    
#     return base*h
# def display_volume(item, volume):
#     print(f"{item} = {volume:.2f} cm3")
# ####################################################################
# def compute_num_box(tank_volume, box_volume):    
#     return tank_volume/box_volume
# def display_num_box(num_box):
#     print(f"Number of boxes = {math.floor(num_box)}")
# ####################################################################
# tank_radius, tank_height = read_two_floats('Enter tank radius (unit=cm): ','Enter tank height (unit = cm): ')
# tank_base = compute_circle_area(tank_radius)
# tank_volume = compute_volume(h=tank_height,base=tank_base)
# display_volume('Lemonade volume', tank_volume)
# box_width, box_length,box_height  = read_three_floats('Enter box width (unit = cm): ','Enter box length (unit = cm): ','Enter box height (unit = cm): ')
# box_base = compute_rectangle_area(box_width, box_length)
# box_volume = compute_volume(base =box_base, h =box_height)
# display_volume("Box volume", box_volume)
# nbox = compute_num_box(tank_volume, box_volume)
# display_num_box(nbox)

# import math
# def read_one_float_item(item): 
#     x =float(input(f"Enter {item} (unit = cm): "))
#     return x
# ####################################################################
# def compute_cylinder_volume(r, h):    
#     return math.pi*(r**2)*h
# def compute_box_volume(w, l, h):
#     return w*l*h
# ####################################################################
# # function get_tank_volume
# #   receives two inputs that are radius and height of tank,
# #   computes and displays tank volume,
# #   and also returns the tank volume.
# def get_tank_volume(radius, height):    
#     tank_volume = compute_cylinder_volume(tank_radius,tank_height)
#     print(f"Lemonade volume = {tank_volume:.2f} cm3")
#     return tank_volume
# ####################################################################
# # function get_box_volume
# #   receives 3 inputs that are width, length, height of box,
# #   computes and displays box volume,
# #   and also returns the box volume.
# def get_box_volume(width, length, height):    
#     box_volume = compute_box_volume(box_width,box_length,box_height)
#     print(f"Box volume = {box_volume:.2f} cm3")
#     return box_volume
# ####################################################################
# def compute_num_box(tank_volume, box_volume):
#     return tank_volume/box_volume
# def display_num_box(num_box):
#     print(f"Number of boxes = {math.floor(num_box)}")
# ####################################################################\
# tank_radius = read_one_float_item('tank radius')
# tank_height = read_one_float_item('tank height')
# ####################################################################
# tank_volume = get_tank_volume(tank_radius, tank_height)
# #####################################################################
# box_width = read_one_float_item("box width")
# box_length = read_one_float_item("box length")
# box_height = read_one_float_item("box height")
# #####################################################################
# box_volume = get_box_volume(box_width, box_length, box_height)

# #####################################################################
# nbox = compute_num_box(tank_volume, box_volume)
# display_num_box(nbox)
def ask_two_side():
    s1 = int(input("Enter first side: "))
    s2 = int(input("Enter second side: "))
    return s1,s2
def get_perimeter(side1,side2):
    perimeter = 2*(side1+side2)
    return perimeter
def get_area(side1,side2):
    area = side1*side2
    return area
def is_square(side1,side2):
    if side1 == side2:
        return True
    else:
        return False
def get_diameter(side):
    diameter = side*(2**0.5)
    return diameter
s1,s2 = ask_two_side()
print(f"Perimeter = {get_perimeter(s1,s2):.2f}")
print(f"Area = {get_area(s1,s2):.2f}")
if is_square(s1,s2)== True:
    print("This is a square.")
    print(f"Diameter = {get_diameter(s1):.2f}")
else:
    print("This is not a square.")