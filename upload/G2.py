n = int(input())
prime = 10**4
boolprime = [True] * (prime+1)
boolprime[0] = boolprime[1] = False
for i in range(2,prime):
        for j in range(2*i,prime+1,i):
            boolprime[j] = False





for i in range(n):
    a = input().split()
    num = 1
    for k in range(int(a[1])+1,int(a[0])+1):
        num*= k 
    n1 = 2
    count = 0
    while num!=1:
        if boolprime[num]:
            count+=1
            break
        while num%n1==0:
            num = num//n1  
            count+=1
        n1+=1
    print(count)            