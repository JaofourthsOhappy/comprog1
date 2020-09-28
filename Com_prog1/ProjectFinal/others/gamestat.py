class Gamestat :
    def __init__(self,id=0,name ="",num_plays = 0 , num_wins = 0):
        self.__id = id
        self.__num_plays = num_plays
        self.__name = name
        self.__num_wins = num_wins
        
    def __str__(self):
        # if self.__name == "Nam tao":
        #     msg = "Lifes"
        # else:
        #     msg = "wins"
        string = ""
        string += f"\n{self.__name}: #plays = {self.__num_plays} #{self.__name} = {self.__num_wins}"
        return string

    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value
    @property
    def num_play(self):
        return self.__num_plays
    @num_play.setter
    def num_play(self,value):
        self.__num_plays = value
    @property
    def num_win(self):
        return self.__num_wins       
    @num_win.setter
    def num_win(self,value):
        self.__num_wins = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
