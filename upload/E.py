a = input().split()
tool = int(a[0])
arz = int(a[1])
people = int(a[2])
mat = []
def mat_change(mat,tool,arz):
    for i in range(arz):
        for j in range(tool):
            if mat[i][j]=='L':
                if i-1<=0:
                    mat[i][j]='.'
                else:
                    mat[i-1][j],mat[i][j] = mat[i][j] , mat[i-1][j]  
            if mat[i][j]=='R':
                if i+1>=arz:
                    mat[i][j]='.'
                else:
                    mat[i][j],mat[i+1][j] = mat[i+1][j] , mat[i][j] 
            if mat[i][j] == 'U':
                if i-1<=0:
                    mat[i][j]= '.'
                else:
                    mat[i-1][j],mat[i][j] = mat[i][j] , mat[i-1][j]
            if mat[i][j] =='D':
                if j+1 >=tool:
                    mat[i][j] = '.'
                else:
                    mat[i][j],mat[i][j+1] = mat[i][j+1],mat[i][j]      
    return mat    
                         
    
for i in range(tool):
    m = input().split()
    mat+=[m]
print(mat)    
print(mat_change(mat,tool,arz))     
#for n in range(arz):
   # for movement in range(arz)
    


