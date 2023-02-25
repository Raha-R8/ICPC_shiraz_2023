n = int(input())
sum = 0
for num in range(1,n//2+1):
    if n%num==0:
        sum+=num
#print(sum)
def isbinary(n):
    if n%2==0 or n==1 :
        for power in range(15):
            if n == 2**power:
                return 1
        return 0
    else:
        return 0
print(isbinary(sum))
#13min
