def isprime(num):
    boolprime = [True] * (num+1)
    boolprime[0] = boolprime[1] = False
    for i in range(2,num):
        if boolprime[i] == True:
            if num % i == 0:
                return False
            for j in range(2*i,num+1,i):
                boolprime[j] = False
    return True




n = int(input())
def least(num):
    if isprime(num):
        return -1
    for i in range(2,num):
        if num%i==0:
            return i 
    return -1   
for i in range(n):
    a = input().split()
    num = 1
    for j in range(int(a[1])+1,int(a[0])+1):
        num*= j 
    count = 1
    while least(num)!=-1:
        num = num//least(num)  
        count+=1
    print(count)      


