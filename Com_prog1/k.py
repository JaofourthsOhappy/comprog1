def check_grid(self,x,y,choose):
    for i in range(len(self.__grid[2])):
            if self.__grid[2][i] == 'X':
                # self.__game_over = True
                for j in choose:
                    if j == i :
                        print("win")
                    else:
                        print("lost")
        
