n = int(input())
mat = []
for num in range(n):
    a = input().split()
    a = [int(x) for x in a]
    mat+=[a]



game_dict = {}
for m in range(n):
    emtiaz = 0
    goal_difference =0
    game_dict[m] = [emtiaz , goal_difference]



for i in range(n):
    for j in range(i+1,n):
        i_goal = mat[i][j]
        j_goal = mat[j][i]
        if i_goal>j_goal:
            game_dict[i][0]+=3
        elif i_goal<j_goal :
            game_dict[j][0]+=3
        elif (i_goal == j_goal) and i!=j:
            game_dict[i][0]+=1
            game_dict[j][0]+=1

        game_dict[i][1]+=i_goal-j_goal
        game_dict[j][1]+=j_goal-i_goal

ans = []
for k,v in game_dict.items():
    team = v+[n-k]
    team = tuple(team)
    ans.append(team)

ans.sort(reverse = True)

ans_num = ''
for i in ans:
    ans_num+=str(i[2])

start = n+97
final_str = ''
for digit in ans_num:
    ascii = start - int(digit)
    final_str+=chr(ascii)
print(final_str)

#73min

























                #
