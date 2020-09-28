import time
# start = time.time()
# time.sleep(3)
# stop = time.time()

def current_time():
    return time.time()

while True :
    menu = input("(S)tart , (e)lapse  , (q)uit")
    if menu == 's' :
        start = current_time()
    elif menu == 'e':
        elaspe = current_time() - start
        print(f"{elaspe:.0f} seconds")
    elif menu == "q" :
        stop = current_time()
        diff = int(stop - start)
        print(f"Total {diff} seconds")
        break
    else:
        print("Incorrect Menu")