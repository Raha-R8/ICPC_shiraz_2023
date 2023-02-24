n = int(input())
inp = list(input())
i = 0
while i < len(inp):
    if i + 1 < len(inp):
        if inp[i] == inp[i+1]:
            del inp[i]
            del inp[i]
            i = 0
            continue
    else:
        break
    i+=1
print("".join(i for i in inp))
