# level 1
# def check_char(char):
#     if char!= 'n'  and char!= 'q' and char != 's' and char != 'N' :
#         print("Incorrect Menu")
#         return False
#     else:
#         return True
# def name_command():
#         input_name = input("Name : ")
#         print(f"{input_name} added")
#         return input_name
# name = []

# while True:
#     char = input("(N)ew (Q)uit: ")
#     if check_char(char) == False:
#         char = input("(N)ew (Q)uit: ")
#     if char == 'N' or char == 'n':
#         input_name = name_command()
#         name.append(input_name)
#         break
# while True:
#     char = input("(N)ew (S)how (Q)uit: ")
#     if char == 'n'or char == 'N':
#         input_name = name_command()
#         name.append(input_name)
#     elif char == 's' or char == 'S':
#             count=1
#             for i in name :
#                 print(f"({count}) {i}")
#                 count +=1
#     elif char == 'q' or char == 'Q':
#             break
#     else:
#         print("Incorrect Menu")
# print("Bye")

# level 2
# def check_char(char):
#     if char!= 'n'  and char!= 'q' and char != 'N' :
#         print("Incorrect Menu")
#         return False
#     else:
#         return True
# def name_command():
#         input_name = input("Name : ")
#         print(f"{input_name} added")
#         return input_name
# name = []

# while True:
#     char = input("(N)ew (Q)uit: ")
#     if check_char(char) == False:
#         char = input("(N)ew (Q)uit: ")
#     if char == 'N' or char == 'n':
#         input_name = name_command()
#         name.append(input_name)
#         break
# while True:
#     char = input("(N)ew (S)how (D)elete (Q)uit: ")
#     if char == 'n'or char == 'N':
#         input_name = name_command()
#         name.append(input_name)
#     elif char == 's' or char == 'S':
#             count=1
#             for i in name :
#                 print(f"({count}) {i}")
#                 count +=1
#     elif char == 'q' or char == 'Q':
#             break
#     elif char == 'd' or char == 'D':
#             delete_num = int(input("Number? : "))
#             name= name[:delete_num-1] + name[delete_num:]
#             count=1
#             for i in name :
#                 print(f"({count}) {i}")
#                 count +=1
#     else:
#         print("Incorrect Menu")
# print("Bye")

# level 3


def new_item(list, item):
    return list.append(item)


def menu_text(list):
    if len(list) < 1:
        char = input("(N)ew (Q)uit: ")
    else:
        char = input("(N)ew (S)how (D)elete (Q)uit: ")
    return char


def show_item(list):
    count = 1
    for i in list:
        print(f"({count}) {i}")
        count += 1


def delete_item(list):
    while True:
        try:
            num = int(input("Number? : "))
            if 0 < num <= len(list):
                list = list[:num-1] + list[num:]
                show_item(list)
                break
            else:
                print("Not in range")
        except:
            print("not a number")


name = []
while True:
    char = menu_text(name)
    if char == 'n' or char == 'N':
        input_name = input("Name : ")
        print(f"{input_name} is added")
        new_item(name, input_name)
    elif char == 'S' or char == 's':
        show_item(name)
    elif char == 'd' or char == 'D':
        delete_item(name)
    elif char == 'q' or char == 'Q':
        print('bye')
        break
