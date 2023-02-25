a = input().split()
num = int(a[0])
o1,o2,o3,o4 = int(a[1]),int(a[2]),int(a[3]),int(a[4])
count = 0
for i in range(num,1,-1):
    if i%o1==0:
        count+=1
    elif i%o2==0:
        count+=1
    elif i%o3==0:
        count+=1
    elif i%o4==0:
        count+=1


print(count)
#5min
