
# def cal_winrate(win,lose):
#     win = int(win)
#     lose = int(lose)
#     return win/(win+lose)
# def print_winrate(list_team,win,lose):
#     for i in range(len(list_team)):
#         winrate = cal_winrate(win[i],lose[i])
#         print(f"{list_team[i]}: got win rate {winrate:.5f}")
#         list_winrate.append(winrate)
# file = input("Enter a file name: ")
# data = open(file).read().splitlines()
# n = int(input("Total team(s): "))
# list_data =[]

# for x in (data):
#     x = x.split(",")
#     list1 =[]
#     for y in x :
#         list1.append(y)
#     list_data.append(list1)
# list_name = []
# list_winrate = []
# for i in range(len(list_data)):
#     list_name.append(list_data[i][0])
# list_win =[]
# for i in range(len(list_data)):
#     list_win.append(list_data[i][1])
# list_lose = []
# for i in range(len(list_data)):
#     list_lose.append(list_data[i][2])

# print_winrate(list_name,list_win,list_lose)
# print("===============")
# for i in range(len(list_winrate)) :
#     if list_winrate[i] == max(list_winrate):
#         print(f"{list_name[i]} got maximum win rate {list_winrate[i]:.5f}")
#     elif list_winrate[i] == min(list_winrate):
#         print(f"{list_name[i]} got minimum win rate {list_winrate[i]:.5f}")





def cal_winrate(win,lose):
    win = int(win)
    lose = int(lose)
    return win/(win+lose)
def print_winrate(list_team,win,lose):
    for i in range(len(list_team)):
        winrate = cal_winrate(win[i],lose[i])
        list_winrate.append(winrate)
    return list_winrate


# def print_order(list_name,list_winrate):
#     list_winrate.sort()
#     for i in range(list_name):
        

file = input("Enter a file name: ")
data = open(file).read().splitlines()
print(f"Total team(s): {len(data)}")
list_data =[]

for x in (data):
    x = x.split(",")
    list1 =[]
    for y in x :
        list1.append(y)
    list_data.append(list1)
list_name = []
list_winrate = []
for i in range(len(list_data)):
    list_name.append(list_data[i][0])
list_win =[]
for i in range(len(list_data)):
    list_win.append(list_data[i][1])
list_lose = []
for i in range(len(list_data)):
    list_lose.append(list_data[i][2])
list_winrate =print_winrate(list_name,list_win, list_lose)
while True :
    option = input("What do you want to know? (m)in , ma(x) , (o)rder max to min, (q)uit : ")
    if option == 'x':
        for i in range(len(list_winrate)) :
            if list_winrate[i] == max(list_winrate):
                print(f"{list_name[i]} got maximum win rate {list_winrate[i]:.5f}")
    elif option == 'm' :
        for i in range(len(list_winrate)) :
            if list_winrate[i] == min(list_winrate):
                print(f"{list_name[i]} got minimum win rate {list_winrate[i]:.5f}")
    elif option == 'o':
        # print_order(list_name,list_winrate)
        pass
    elif option == 'q':
        print("Bye")
        break
