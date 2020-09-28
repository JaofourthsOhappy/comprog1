# m = int(input("Enter m: ")) 
# hello = 0
# bye = 0
# while m>0:     
#     n = int(input("Enter n: "))
#     for i in range(m):
#         print(f'Hello #{i}')
#         hello += 1
#     for i in range(n):
#         print(f'Bye {m-1} {i}')  
#         bye += 1 
#     m = int(input("Enter m: ")) 
# else:
#     print(f'You print Hello for {hello} lines')   
#     print(f"You print Bye for {bye} lines")     


     
# m = int(input("Enter m: "))
# hello = 0
# bye = 0
# while m>0:     
#     n = int(input("Enter n: "))
#     for i in range(n):
#         print(f'Bye #{i}')
#         bye += 1 
#         for j in range(m):
#             print(f'Hello {j} {i}')  
#             hello += 1 
#     m = int(input("Enter m: "))     
# else:
#     print(f'You print Hello for {hello} lines')   
#     print(f"You print Bye for {bye} lines")     

def print_field(field,symbols):
    for i in range(len(field[0])):
        print('--', end='')  
    print('-')     

    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 0:
                print('| ',end='')
            elif field[i][j] == -1:
                print('|X',end='')    
            else:                    
                index = field[i][j] - 1
                print(f'|{symbols[index]}',end='') 
        print('|')        

    for i in range(len(field[0])):
        print('--', end='')  
    print('-') 

def get_submarine_info(field, sub_names):
    orig_sizes = {name:0 for name in sub_names}
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != 0:
                index = field[i][j] -1
                orig_sizes[sub_names[index]] +=1


    curr_sizes = dict(orig_sizes)            
    statuses = {x:'T' for x in sub_names}

    return orig_sizes,curr_sizes,statuses

def display_result(sub_names,orig_sizes,curr_sizes,statuses):
    print('Submarine name:', end='') 
    for name in sub_names:
        print(f'{name:>10}',end='')  
    print('\nOriginal size :', end='')  
    for name in sub_names:
        print(f'{orig_sizes[name]:>10}',end='') 
    print('\nCurrent size  :', end='')       
    for name in sub_names:
        print(f'{curr_sizes[name]:>10}',end='')
    print('\nStatus        :', end='')        
    for name in sub_names:
        print(f'{statuses[name]:>10}',end='')           
    print()

def get_attack_position(field):
    check = True
    while check == True:
        x = int(input(f'Enter x position (1-{len(field[0])}): '))
        if x in range(1,len(field[0])+1):
            check = False
        else:
            print('Invalid x position!') 

    check = True
    while check == True:               
        y = int(input(f'Enter y position (1-{len(field)}): '))
        if y in range(1,len(field)+1):
            check = False
        else:
            print('Invalid y position!')

    return x,y


def update(x,y,field,sub_names,curr_sizes,statuses):
    rowindex = y-1
    columnindex = x-1
    index = field[rowindex][columnindex] - 1

    if field[rowindex][columnindex] == -1 :
        curr_sizes[sub_names[index]] += 0
    else:
        if index != -1:
            curr_sizes[sub_names[index]] += -1
        else:
            curr_sizes[sub_names[index]] += 0

    if curr_sizes[sub_names[index]] == 0:
        statuses[sub_names[index]] = 'F'

    field[rowindex][columnindex] = -1



import math

field = [[3, 0, 1, 1, 1],
         [3, 0, 0, 0, 0], 
         [3, 3, 0, 0, 0],
         [0, 2, 2, 2, 0],
         [0, 0, 2, 0, 0],
         [0, 0, 0, 0, 0]]

symbols = ['@', '#', '&', '$', 'N'] 

sub_names = ['Marlin','Nautilus','Seawolf']


round = 1

print_field(field,symbols)  
orig_sizes,curr_sizes,statuses = get_submarine_info(field,sub_names)
display_result(sub_names, orig_sizes,curr_sizes,statuses)

print(f'Attack #{round}:')
x,y = get_attack_position(field)
round += 1

while True:
    update(x,y,field,sub_names,curr_sizes,statuses)
    print_field(field,symbols)   
    display_result(sub_names,orig_sizes,curr_sizes,statuses)
    subdestory = 0
    for i in statuses:
        if statuses[i] == 'F':
            subdestory += 1
    if subdestory == 2:
        print(f'Congratulations, you attacked {math.ceil(len(sub_names)/2)} out of {len(sub_names)} submarines')
        print(f'You attacked {round-1} times.')
        break        
    else:
        print(f'Attack #{round}:')
        round += 1
        x,y = get_attack_position(field)

