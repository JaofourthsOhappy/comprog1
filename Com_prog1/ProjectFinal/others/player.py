from gamestat import Gamestat

class Player :
    def __init__(self,name = "" ,balance =0):
        self.__name = name
        self.__balance =balance
        # self.__game_stat_list = [[self.__game_stat.get_num_win(), self.__game_stat.get_num_play() ]for i in range(3)]
        self.__game_stat_list =[Gamestat(1,"Black Jack",0,0),Gamestat(2,"Nam tao",0,0),Gamestat(3,"Ladder",0,0)]
    def __str__(self):
        string = ""
        string += f"{self.__name}: Balance = {self.__balance:.2f}"
        for i in range(3):
            string+= str(f"{self.__game_stat_list[i]}")
        return string
    def find_game_stat(self,game_id):
        for i in range(len(self.__game_stat_list)) :
            if i == game_id-1 :
                return self.__game_stat_list[i]
    def update_num_play(self,game_id):
        # game_id = self.__game_stat_list[game_id-1]
        # if game_id == 1 :
        game = self.__game_stat_list[game_id-1]
        game.num_play +=1
        # print(self.__game_stat_list[game_id-1])

    def update_num_win(self,game_id,win_value):
        game = self.__game_stat_list[game_id-1]
        # game.set_num_win(game.get_num_play()+win_value)
        game.num_win += win_value
    def update_balance(self,added):
        self.__balance += added
    
    @property
    def game_stat_list(self):
        return self.__game_stat_list
    @game_stat_list.setter
    def game_stat_list(self,value):
        self.__game_stat_list = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name =value
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        self.__balance = value        

# player1 = Player("kao",1000)
# print(player1)
# print()
# player1.update_num_win(1,2)
# player1.update_num_play(1)
# print(player1)