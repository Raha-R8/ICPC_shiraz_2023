n = int(input())
str = list(input())
def finish(str):
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            return True
    return False
while finish(str):
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            str = str[:i]+str[i+2:]
            break
print(''.join(str))
#13min
