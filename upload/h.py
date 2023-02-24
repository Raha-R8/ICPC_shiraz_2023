n = int(input())
m = int(input())
mod = n * m
num1 = int(input())
num2 = int(input())
num3 = num1 + num2
if num3 == 0:
    print("0")
elif num3 % mod == 0:
    print(mod)
else:
    print(num3 % mod)



