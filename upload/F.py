def check(n,sorted,list):
    if (list[:n]).sort()==sorted[:n]:
        return True
n = int(input()) 
num_list = input().split()
num_list = [int(x) for x in num_list]
sort = num_list.sort()
i = 2
while num_list!=None:
    count = 0
    if check(i,sort,num_list):
        num_list=num_list[i:]
        count+=1
        i =1
    i+=1    
print(count)