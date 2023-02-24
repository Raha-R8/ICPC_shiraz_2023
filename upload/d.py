n = int(input())
matrix = []
for i in range(n):
    matrix += [[int(i) for i in input().split()]]

list3d = [[0,0,0]] * n
dict = {}
f = 0
for i in range(26,26-n,-1):
    dict[i] = chr(ord("a") +f )
    f += 1
f = 0
for i in range(26,26-n,-1):
    list3d[f] = [0,0,i]
    f += 1
for i in range(n):
    for j in range(n):
        if matrix[i][j] > matrix[j][i]:
            list3d[i][0] += 3
        
        elif matrix[i][j] == matrix[j][i] and i !=j:
            list3d[i][0] += 1
        list3d[i][1] += matrix[i][j] - matrix[j][i]
for i in range(n):
    list3d[i] = tuple(list3d[i])
list3d.sort()
for i in range(n):
    list3d[i] = list(list3d[i])
    list3d[i][2] = dict[list3d[i][2]]

strn = ""
for i in range(n-1,-1,-1):
    strn+=list3d[i][2]
print(strn)