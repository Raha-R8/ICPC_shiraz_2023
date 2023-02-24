
n = int(input())
sum = 0
if n != 1:
    for i in range(1,n):
        if n % i == 0:
            sum +=i

    numcopy = sum

    while (numcopy %2) !=1:
        numcopy = numcopy / 2
    if numcopy == 1:
        print("1")
    else:
        print("0")
if n == 1:
    print("0")