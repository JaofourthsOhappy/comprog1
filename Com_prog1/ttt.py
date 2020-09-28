class Player :
    def __init__(self,name = "" ,balance =0):
        self.__name = name
        self.__balance =balance
        # self.__game_stat_list = [[self.__game_stat.get_num_win(), self.__game_stat.get_num_play() ]for i in range(3)]
        self.__game_stat_list =[Gamestat(1,"Black Jack",0,0),Gamestat(2,"Nmm tao",0,0),Gamestat(3,"Ladder",0,0)]
    def __str__(self):
        string = ""
        string += f"{self.__name}: Balance = {self.__balance:.2f}"
        for i in range(3):
            string+= str(f"{self.__game_stat_list[i]}")
        return string
    def find_game_stat(self,game_id):
        for i in range(len(self.__game_stat_list)) :
            if i == game_id :
                pass
    def update_num_play(self,game_id):
        # game_id = self.__game_stat_list[game_id-1]
        # if game_id == 1 :
        game = self.__game_stat_list[game_id-1]
        game.set_num_play(game.get_num_play()+1)
        # print(self.__game_stat_list[game_id-1])

    def update_num_win(self,game_id,win_value):
        game_id = self.__game_stat.get_id()
        if game_id == 1 :
            self.__game_stat.set_num_win(self.__game_stat.get_num_win()+1)
    def update_balance(self,game_id):
        pass
    def print_list(self):
        for i in self.__game_stat_list :
            print(i)

    def set_name(self,value):
        self.__name =value
    def get_name(self):
        return self.__name
    def set_balance(self,value):
        self.__balance = value
    def get_balance(self):
        return self.__balance
        
class Gamestat :
    def __init__(self,id=0,name ="",num_plays = 0 , num_wins = 0):
        self.__id = id
        self.__num_plays = num_plays
        self.__name = name
        self.__num_wins = num_wins
        
    def __str__(self):
        string = ""
        string += f"\n{self.__name}: #plays = {self.__num_plays} #wins = {self.__num_wins}"
        return string

    def get_id(self):
        return self.__id
    def set_id(self,value):
        self.__id = value
    def set_num_play(self,value):
        self.__num_plays = value
    def get_num_play(self):
        return self.__num_plays
    def set_num_win(self,value):
        self.__num_wins = value
    def get_num_win(self):
        return self.__num_wins        
    def set_name(self,value):
        self.__name = value
    def get_name(self):
        return self.__name

class PlayerHandler : 
    def __init__(self):
        self.__list_player = []
        # self.__file = open()
    def read_from_file(self):
        pass
    def write_to_file(self):
        pass

    def show_player(self):
        for i in self.__list_player :
            print(i)
    def add_new_player(self,name,balance):
        self.__list_player.append()
    def search_player(self):
        for i in self.__list_player:
            pass

    def add_balance(self):
        pass
 

player1 = Player("Kao" ,1000)
player1.update_num_play(1)
player2 = Player("Pun",1000)
player2.update_num_play(2)
# player2.update_num_play(1)
# player1.update_num_play(2)
# player1.update_num_play(3)
print(player1)
print()
print(player2)