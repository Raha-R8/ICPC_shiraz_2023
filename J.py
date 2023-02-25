a = input().split()
animal_count  = int(a[0])
blanket = int(a[1])
animals = input().split()
animals = [int(x) for x in animals]
animals.sort()
#print(animals)
blanket_count = 0
while len(animals)>0:
    i = 0
    j = 1
    if len(animals)>1 and  animals[j]-animals[i]<=blanket:
        while animals[j]-animals[i]<=blanket:
            j+=1
        blanket_count+=1
        animals = animals[j:]
    else:
        blanket_count+=1
        animals = animals[j:]
print(blanket_count)
#25min
