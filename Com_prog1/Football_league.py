played_team = {}
score_list =[]
score_in_table = []

def check_if_dup(team1,team2):
    if team1 in played_team and team2 in played_team :
        return True
    else:
        return False

def seperate_data(msg):
    return msg[0] , msg[-1] , msg[1][0] ,msg[1][-1]

def add_data(team1, team2 ,team1_point , team2_point): 
    played_team[team1] =0
    played_team[team2] =0
    else:
        played_team[team1] += team1_point
        played_team[team2] += team2_point
def cal_score(team1,team2):
    if team1 > team2 :
        point_team1 = 3
        point_team2 = 0
    elif team1 == team2 :
        point_team1 = 1
        point_team2 = 1
    else:
        point_team1 = 0
        point_team2 = 3
    return point_team1 , point_team2


match_result = input("Match result: ")
while match_result != 'exit 0:0 exit' :
    match_result = match_result.lower()
    new_match_result = match_result.split(' ')
    team1,team2,score_team1 ,score_team2 = seperate_data(new_match_result)

    if check_if_dup(team1,team2) :
        print("Error!! This match is duplicated.")
    else:
        point_team1 , point_team2 =cal_score(score_team1,score_team2)
        add_data(team1,team2,point_team1,point_team2)
        print(f"{team1} get {point_team1} point, {team2} get {point_team2} point")

    print()
    match_result = input("Match result: ")


print("--------------- League Table information ------------------")
print()
for team in played_team :
    print(team, '=' , played_team[team] , 'point')