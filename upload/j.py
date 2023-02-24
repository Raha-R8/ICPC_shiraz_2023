tedadtul = input().split()
n, length = int(tedadtul[0]), int(tedadtul[1])
animals = [int(i) for i in input().split()]
animals.sort()
list1 = [0] * (max(animals)+1)
count = 0
for i in animals:
    if list1[i] == 0:
        for j in range(i,i+length+1):
            if j < len(list1):
                list1[j] = 1
        count += 1
print(count)