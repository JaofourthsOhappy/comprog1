from player import Player
import sys
import os
sys.path.insert(1,"ProjectFinal")
folder = os.getcwd()
files =os.listdir(folder)
class Error(Exception):
    pass
class AccountNotFound(Error):
    pass

class PlayerHandler : 
    def __init__(self):
        self.__list_player =[]

    @property
    def list_player(self):
        return self.__list_player
    @list_player.setter
    def list_player(self,value):
        self.__list_player = value

    def read_from_file(self):
        lines = open(os.path.join("others/output.txt")).read().splitlines()
        
    def write_to_file(self):
        file = open(os.path.join("others/output.txt"),'w')
        for player in self.__list_player:
            file.write(f"{player}\n")
        file.close()
        
    def show_player(self):
            for i in self.__list_player :
                print(i)
                print()

    def add_new_player(self,player):
            try: 
                index  = self.search_player(player.name)
                player = self.__list_player[index]

            except AccountNotFound:
                self.__list_player.append(player)
            return player
    def search_player(self,name):
        for i in range(len(self.__list_player)):
            if self.__list_player[i].name == name :
                return i
        raise AccountNotFound
    def add_balance(self,name,added):
        try :
            index = self.search_player(name)
            self.__list_player[index].balance += added
        except AccountNotFound:
            print("Can't Find this account")

    def get_list(self):
        return self.__list_player