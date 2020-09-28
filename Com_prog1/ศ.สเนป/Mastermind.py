import random
def check(guess,ans):
    list_ = []
    correct = ""
    ans1 = list(ans)
    for char in guess :
        list_.append(int(char))
    for i in range(len(list_)) :
        if list_[i] in ans1:
            correct += 'o'
            ans1.remove(list_[i])
    return correct

def check_pos(guess,ans,o):
    list_ = []
    answer = ''
    ans2 = list(ans)
    for char in guess :
        list_.append(int(char))
    for i in range(len(guess)):
        if list_[i] == ans2[i]:
            answer+= '*'
    return answer 

def  random_num():
    ans = []
    for time in range(4):        
        num = random .randint(0,6)
        ans.append(num)    
    return ans
#*main
COLOR = [1,2,3,4,5,6]
ANS = random_num()
count_round = 0
while True: 
    guess = input("What is your guess?: ")
    print(f"Your guess is {guess}")
    correct_color = check(guess,ANS)
    correct_pos = check_pos(guess,ANS,correct_color)
    print(ANS)
    if len(correct_pos) == 4:
        print(correct_pos)
        break
    elif len(correct_pos) != 0:
        correct = correct_pos +correct_color[0:len(correct_color)-len(correct_pos)]
        print(correct)
    else:
        print(correct_color)
    count_round+=1

print(f"You are correct after {count_round} rounds")