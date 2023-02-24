n = int(input())
string = input()
inp = []
for i in string:
    inp +=[i]
for i in inp:
    if inp[i] == inp[i+1]:
        del inp[i]
        del inp [i+1]

print(inp)