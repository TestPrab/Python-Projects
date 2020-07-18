def edit_distance(stat1,stat2):
    len1=len(stat1)
    arr=[[0 for i in range(len1+1)]  for x in range (2)]
    for i in range(len1+1):
        arr[0][i]=i
    for i in range(1,len(stat2)+1):
        for j in range(len1+1):
            if(j==0):
                arr[i%2][j]=i
            elif(stat1[j-1]==stat2[i-1]):
                arr[i%2][j]=arr[(i-1)%2][j-1]
            else:
                arr[i%2][j]=1+min(arr[(i-1)%2][j],min(arr[(i-1)%2][j-1],arr[i%2][j-1]))
    return arr[len(stat2)%2][len1]
st1=input()
st2=input()
print(edit_distance(st1,st2))
