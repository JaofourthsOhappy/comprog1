#level1 
# def input_point(msg):
#     x = int(input(f"Enter x{msg} :"))
#     y = int(input(f"Enter y{msg} :"))
#     return x,y
# x1,y1 = input_point("1")
# x = []
# y = []
# x.append(x1)
# y.append(y1)
# count = 1
# command = input("(m)ore, (e)nd :")
# while command != 'e':
#         count+=1
#         x_co,y_co = input_point(f"{count}")
#         x.append(x_co)
#         y.append(y_co)
#         command = input("(m)ore, (e)nd :")
# command_2 = input("(s)how points, (q)uit :")
# count_point=1
# while True:
#     if command_2== 's':
#         for coor in range(len(x)) :
#             print(f"Point{count_point} = ({x[coor]},{y[coor]})")
#             count_point +=1
#     elif command_2 == 'q' :
#         print("Bye")
#         break
#     command_2 = input("(s)how points, (q)uit :")


# #level2
# import math
# def cal_distance(x1,y1,x2,y2):
#     distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
#     print(f"Distance from P1 to P2 is {distance:.2f}")
# def input_point(msg):
#     x = int(input(f"Enter x{msg} :"))
#     y = int(input(f"Enter y{msg} :"))
#     return x,y
# def inputx_y ():    
#     x1,y1 = input_point("1")
#     x = []
#     y = []
#     x.append(x1)
#     y.append(y1)
#     count = 1
#     command = input("(m)ore, (e)nd :")
#     while command != 'e':
#             count+=1
#             x_co,y_co = input_point(f"{count}")
#             x.append(x_co)
#             y.append(y_co)
#             command = input("(m)ore, (e)nd :")
#     return x,y

# x,y =inputx_y()
# command_2 = input("(s)how points, (d)istance, (n)ew, (q)uit :")
# count_point=1
# while True:
#     if command_2== 's':
#         for coor in range(len(x)) :
#             print(f"Point{count_point} = ({x[coor]},{y[coor]})")
#             count_point +=1
#     elif command_2 == 'd':
#         cal_distance(x[0],y[0],x[1],y[1])
#     elif  command_2 == 'n':
#         x,y = inputx_y()
#     elif command_2 == 'q' :
#         print("Bye")
#         break
#     command_2 = input("(s)how points, (d)istance, (n)ew, (q)uit :")


# #level3
# import math
# def cal_distance(x1,y1,x2,y2):
#     distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
#     return distance
# def cal_perimeter(x,y):
#     peri = []
#     count =1
#     for i in range(len(x)):
#         if count < len(x):
#              distance = cal_distance(x[i],y[i],x[i+1],y[i+1])
#              peri.append(distance)
#         count += 1
#     else:    
#         distance = cal_distance(x[i],y[i],x[0],y[0])
#     peri.append(distance)
#     return peri
# def input_point(msg):
#     x = int(input(f"Enter x{msg} :"))
#     y = int(input(f"Enter y{msg} :"))
#     return x,y
# def inputx_y ():    
#     x1,y1 = input_point("1")
#     x = []
#     y = []
#     x.append(x1)
#     y.append(y1)
#     count = 1
#     command = input("(m)ore, (e)nd :")
#     while command != 'e':
#             count+=1
#             x_co,y_co = input_point(f"{count}")
#             x.append(x_co)
#             y.append(y_co)
#             command = input("(m)ore, (e)nd :")
#     return x,y

# x,y =inputx_y()
# count_point=1
# while True:
#     if len(x) <2 :
#         command_2 = input("(s)how points, (n)ew, (q)uit :")
#         if command_2== 's':
#             for coor in range(len(x)) :
#                 print(f"Point{count_point} = ({x[coor]},{y[coor]})")
#                 count_point +=1
#         elif  command_2 == 'n':
#             x,y = inputx_y()
#         elif command_2 == 'q' :
#             print("Bye")
#             break
#     elif len(x) == 2 :
#         command_2 = input("(s)how points, (d)istance, (n)ew, (q)uit :")
#         if command_2== 's':
#             for coor in range(len(x)) :
#                 print(f"Point{count_point} = ({x[coor]},{y[coor]})")
#                 count_point +=1
#         elif command_2 == 'd':
#             distance =cal_distance(x[0],y[0],x[1],y[1])
#             print(f"Distance from P1 to P2 is {distance:.2f}")
#         elif  command_2 == 'n':
#             x,y = inputx_y()
#         elif command_2 == 'q' :
#             print("Bye")
#             break
#     else:
#         command_2 = input("(s)how points, (p)erimeter, (n)ew, (q)uit :")
#         if command_2== 's':
#             for coor in range(len(x)) :
#                 print(f"Point{count_point} = ({x[coor]},{y[coor]})")
#                 count_point +=1
#         elif command_2 == 'p':
#             perimeter = cal_perimeter(x,y)
#             print(f"Perimeter is {sum(perimeter):.2f}")
#         elif  command_2 == 'n':
#             x,y = inputx_y()
#         elif command_2 == 'q' :
#             print("Bye")
#             break



#level4 
import math
def cal_distance(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distance
def cal_perimeter(x,y):
    peri = []
    count =1
    for i in range(len(x)):
        if count < len(x):
             distance = cal_distance(x[i],y[i],x[i+1],y[i+1])
             peri.append(distance)
        count += 1
    else:    
        distance = cal_distance(x[i],y[i],x[0],y[0])
    peri.append(distance)
    return peri
def cal_area(x,y):
    total_area = []
    count =1
    for i in range(len(x)):
        if count < len(x):
            area =(x[i]*y[i+1] )-(y[i]*x[i+1])
            total_area.append(area)
        count+=1
    arealast = (x[-1]*y[0]) -(y[-1]*x[0])
    total_area.append(arealast)
    return total_area
def input_point(msg):
    x = int(input(f"Enter x{msg} :"))
    y = int(input(f"Enter y{msg} :"))
    return x,y
def inputx_y ():    
    x1,y1 = input_point("1")
    x = []
    y = []
    x.append(x1)
    y.append(y1)
    count = 1
    command = input("(m)ore, (e)nd :")
    while command != 'e':
            count+=1
            x_co,y_co = input_point(f"{count}")
            x.append(x_co)
            y.append(y_co)
            command = input("(m)ore, (e)nd :")
    return x,y

x,y =inputx_y()
count_point=1
while True:
    if len(x) <2 :
        command_2 = input("(s)how points, (n)ew, (q)uit :")
        if command_2== 's':
            for coor in range(len(x)) :
                print(f"Point{count_point} = ({x[coor]},{y[coor]})")
                count_point +=1
        elif  command_2 == 'n':
            x,y = inputx_y()
        elif command_2 == 'q' :
            print("Bye")
            break
    elif len(x) == 2 :
        command_2 = input("(s)how points, (d)istance, (n)ew, (q)uit :")
        if command_2== 's':
            for coor in range(len(x)) :
                print(f"Point{count_point} = ({x[coor]},{y[coor]})")
                count_point +=1
        elif command_2 == 'd':
            distance =cal_distance(x[0],y[0],x[1],y[1])
            print(f"Distance from P1 to P2 is {distance:.2f}")
        elif  command_2 == 'n':
            x,y = inputx_y()
        elif command_2 == 'q':
            print("Bye")
            break
    else:
        command_2 = input("(s)how points, (p)erimeter, (a)rea, (n)ew, (q)uit :")
        if command_2== 's':
            for coor in range(len(x)) :
                print(f"Point{count_point} = ({x[coor]},{y[coor]})")
                count_point +=1
        elif command_2 == 'p':
            perimeter = cal_perimeter(x,y)
            print(f"Perimeter is {sum(perimeter):.2f}")
        elif command_2 == 'a':
            area = cal_area(x,y)
            area = math.fabs(sum(area)/2)
            print(f"Area is {area:.2f}")
        elif  command_2 == 'n':
            x,y = inputx_y()
        elif command_2 == 'q' :
            print("Bye")
            break

