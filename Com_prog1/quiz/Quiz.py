class Football:
    def __init__(self,short= "",full = "",win=0 , draw=0 ,lose=0 ):
        self.__short_name = short
        self.__full_name = full
        self.__win = win
        self.__draw = draw
        self.__lose = lose
    
    def won(self,team):
        self.__win += 1
        team.__lose += 1
        
    def drew(self,team):
        self.__draw +=1
        team.__draw +=1

    def losed(self,team):
        self.__lose +=1
        team.__win +=1

    def __str__(self):
        return f"{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}"

    @property
    def win(self):
        return self.__win
    @win.setter
    def win(self,win):
        self.__win = win

    @property
    def lose(self):
        return self.__lose
    @lose.setter
    def lose(self,lose):
        self.__lose = lose   

    @property
    def draw(self):
        return self.__draw    
    @draw.setter
    def draw(self,draw):
        self.__draw = draw

# level1
# ARS = Football("ARS","Arsenal")
# print(ARS)
# ARS.win = 1
# print(ARS)
# ARS.draw = 4
# print(ARS)
# ARS.lose = 2
# print(ARS)
# print()
# LIV =Football("LIV","Liverpool",1,3,4)
# print(LIV)
# LIV.win = 3
# print(LIV)
# LIV.draw = 1
# print(LIV)
# LIV.lose = 6
# print(LIV)

#level2
# ARS = Football("ARS","Arsenal")
# LIV =Football("LIV","Liverpool")
# print(ARS)
# print(LIV)
# print()
# ARS.won(LIV)
# print(ARS)
# print(LIV)
# print()
# LIV.drew(ARS)
# print(ARS)
# print(LIV)
# print()
# ARS.losed(LIV)
# print(ARS)
# print(LIV)
# print()

# CHE = Football("CHE" , "Chelsea")
# MUN = Football("MUN" , "Manchester United")
# MCI = Football("MCI","Manchester City")

# print(CHE)
# print(MUN)
# print(MCI)

# MCI.losed(CHE)
# print(CHE)
# print(MUN)
# print(MCI)
# MUN.won(MCI)
# print(CHE)
# print(MUN)
# print(MCI)

#level 3

class ReadFile :
    def __init__(self,filename = ""):
        self.__filename = filename

    def read(self):
        team = []        
        lines =  open(self.__filename).read().splitlines()        
        table = [x.split(",") for x in lines if x!= ""]
        for row in table :
            team.append(Football(row[0],row[1]))
        return team ,table

    def identify_team(self,input_team):
        print(self.team)
        for i in range(len(self.team)):
            print(self.team[i])
            if self.team[i] == input_team :
                return self.team[i]


short_name = []
filename = input("Please enter a file name: ")
team = ReadFile(filename)
all_team , table= team.read()
print("Menu:")
option = input("(s)how summary (e)nter results (q)uit: ")
while option != 'q':
    if option == 's':
        for team in all_team:
            print(team)
    elif option == 'e' :
        match_result = input("Enter a result : ")
        result = match_result.split(" ")
        if result[1] == 'won':
            for i in range(len(all_team)):
                    if table[i][0] == result[0]:
                        team1 = all_team[i]
                    if table[i][0] == result[2]:
                        team2 = all_team[i]
            team1.won(team2)
        elif result[1] == 'drew':
            for i in range(len(all_team)):
                if table[i][0] == result[0]:
                    team1 = all_team[i]
                if table[i][0] == result[2]:
                    team2 =all_team[i]
            team1.drew(team2)
        elif result[1] == 'losed' :
            for i in range(len(all_team)):
                if table[i][0] == result[0]:
                    team1 = all_team[i]
                if table[i][0] == result[2]:
                    team2 =all_team[i]
            team1.losed(team2)


    print("Menu:")
    option = input("(s)how summary (e)nter results (q)uit: ")