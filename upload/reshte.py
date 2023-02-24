n = int(input())
reshte = input()
reshte = list(reshte)
def check(str):
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            return True
    return False
while check(reshte):
    for i in range(len(reshte)-1):
        if reshte[i]==reshte[i+1]:
            reshte.remove(reshte[i])
            reshte.remove(reshte[i+1]) 
print(reshte)               