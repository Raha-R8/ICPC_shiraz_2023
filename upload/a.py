inp = input().split()
n = int(inp[0])
list1 = []
for i in range(1,len(inp)):
    list1 += [int(inp[i])]
count=0
for i in range(1,n+1):
    for j in list1:
        if i%j==0:
            count+=1
            break
print(count)