import time
class Route :
    __list_name = []
    def __init__(self,name = ""):
        self.__name = name
    def add_route(self):
        name = input("Enter route name : ")
        self.__list_name.append(name)
    def print_route(self):
        for route in range(len(self.__list_name)) :
            print(f"Route{route+1} : {self.__list_name[route]} ")
    def choose (self):
        choose = int(input("Enter a route number : "))
        return choose
    def print_one_name(self,num):
        return self.__list_name[num-1]

class Bus:
    __list_bus = []
    def __init__(self , status = 'stop' , bus_code = "" , start_time = time.time() ):
        self.__bus_code = bus_code
        self.__status = status
        self.__time = start_time
        self.__status = 'Stop'
    def add_bus(self):
        bus = input("Bus code: ")
        self.__list_bus.append(bus)
    def print_bus(self):
        for bus in range(len(self.__list_bus)):
            print(f"{bus+1}. {self.__list_bus[bus]} is {self.__status} (Current  {self.time()} secs / {self.time()} All  secs) ")
    def time(self,option =False):
        if option :
            elaspe = time.time() - elaspe
        else:
            start = time.time()
            elaspe = time.time()- start    
        return f"{elaspe:.0f}"

    def running(self,time):
        bus_num = int(input("Bus number ? "))
        start = time.time()
        current = time - start
        return current
    def status(self):
        return self.__status 
    def stop(self):
        pass
    
#main
while True :
    menu = input("(n)ew Route ,(s)how, (c)hoose ,(q)uit: ")
    if menu == 'n':
        route_name = Route()
        route_name.add_route()
    elif menu == 's':
        route_name.print_route()
    elif menu == 'c' :
        choose = route_name.choose()
        while True :
            option = input("(a)dd bus , (p)rint , (r)un/stop ,(m)ain menu : ")
            if option == "a" :
                bus = Bus()
                bus.add_bus()
            elif option == 'p':
                print(f"Route{choose}: {route_name.print_one_name(choose)}")
                bus.print_bus()
            elif option == 'r':
                start = time.time()
                bus.running(start)
            elif  option == 'm':
                break
            else:
                print("Wrong input !")
    elif menu == 'q':
        break
    else:
        print("Wrong input!")