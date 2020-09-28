# * Submarine
field = [[3, 0, 1, 1 ,1],
             [3, 0, 0, 0, 0],
             [3, 3, 0, 0, 0],
             [0, 2, 2, 2, 0],
             [0, 0, 2, 0, 0],
             [0, 0, 0, 0, 0]]
symbols = ['@' , '#' , '&' , '$' , 'N']
sub_names = ['Marlin' , 'Nautilus' , 'Seawolf']

def print_field (field,symbols):    
    for i in range(len(field[0])):
        print('--' , end= '')
    print('-')
    for i in range(len(field)):
        for j in field[i]:
            # index = field[i][j]+1
            if j == 0 :
                print(f"| " , end = '')
            elif j == -1 :
                print(f"|X" ,end ='')
            else:
                print(f"|{symbols[j-1]}" , end = '')
        print("|")
    for i in range(len(field[0])):
        print('--' , end= '')
    print('-')

def get_submarine_info (field, sub_names):
    orig_sizes = {x:0 for x in sub_names}
    for row in field :
        for i in row :
            if i != 0:
                sub_index = i-1
                orig_sizes[sub_names[sub_index]] = orig_sizes[sub_names[sub_index]] +1
    curr_sizes = dict(orig_sizes)
    statuses = {x:'T' for x in sub_names}
    return orig_sizes , curr_sizes , statuses

def display_result(sub_names , orig_sizes , curr_sizes ,statuses):
    print("Submarine name:" , end = '')
    for name in sub_names :
        print(f"{name:>10}" , end= '')
    print("\nOriginal size :" , end ='')
    for name in orig_sizes:
        print(f"{orig_sizes[name]:>10}", end = '')
    print("\nCurrent size  :" , end = '')
    for name in curr_sizes:
        print(f"{curr_sizes[name]:>10}", end = '')
    print("\nStatus        :", end= '')
    for name in statuses:
        print(f"{statuses[name]:>10}", end = '')

def get_attack_position(field):
    x = int(input(f"Enter x position (1-{len(field[0])}): "))
    while x <1 or x > len(field[0]):
        print("Invalid x position!")
        x = int(input(f"Enter x position (1-{len(field[0])}): "))
    y = int(input(f"Enter y position (1-{len(field)}): "))
    while y <1 or y > len(field):
        print("Invalid y position!")
        y = int(input(f"Enter y position (1-{len(field)}): "))
    return x,y
    # try:
    #     x =(input(f"Enter x position (1-{len(field[0])}): "))
    # except :
    #     print("Invalid x position!")
    # try:
    #     y =(input(f"Enter y position (1-{len(field)}): "))
    # except:
    #     print("Invalid y position!")


    # return int(x),int(y)    

def update(field,sub_names,x,y,curr_sizes,statuses):

    # destroyed_index = field[row][column]-1
    # if destroyed_index == -1 :
    #     curr_sizes[sub_names[destroyed_index]] +=0
    # elif destroyed_index  >=0 :
    #     curr_sizes[sub_names[destroyed_index]] += -1
    # else:
    #     curr_sizes[sub_names[destroyed_index]] += 0
    # if curr_sizes[sub_names[destroyed_index]] == 0:
    #     statuses[sub_names[destroyed_index]] = 'F'
    # field [row][column] = -1    
    row = y-1
    column = x-1
    if field[row][column] >0 :
        destroyed_index = field[row][column]
        name = sub_names[destroyed_index-1]
        curr_sizes[name] += -1
        if curr_sizes[name] == 0:
            statuses[name]  = 'F'
    field[row][column]

import math

orig_sizes , curr_sizes , statuses = get_submarine_info(field,sub_names)
print_field(field , symbols)
count_attack = 1
while True:
    display_result(sub_names,orig_sizes,curr_sizes,statuses)
    print()
    print(f"Attack #{count_attack}:")
    x,y = get_attack_position(field)
    update(field,sub_names,x,y,curr_sizes,statuses)
    print_field(field , symbols)
    check = 0
    for i in statuses :
        if statuses[i] ==  'F':
            check+=1
    if check == 2 :
        display_result(sub_names,orig_sizes,curr_sizes,statuses)
        print()
        break
    count_attack+=1

print(f"Congratulations, you attacked {math.ceil(len(sub_names)/2)} out of {len(sub_names)} submarines")
print(f"You attacked {count_attack} times.")


