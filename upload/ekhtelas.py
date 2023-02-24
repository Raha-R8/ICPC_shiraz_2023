n = int(input())
ans = {}
for i in range(n):
    a = input().split()
    name = a[0]
    ekhtelas = int(a[1])
    if name in ans:
        if ekhtelas>ans[name]:
            ans[name] = ekhtelas
    else:
        ans[name] = ekhtelas
max_ekhtelas = max(ans.values())
for k,v in ans.items():
    if v == max_ekhtelas : 
        print(k)          
    

    

