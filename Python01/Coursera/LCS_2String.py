p=int(input())
stat1=input().split()
m=len(stat1)
q=int(input())
stat2=input().split()
n=len(stat2)
arr=[[ 0 for i in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    for j  in range(n+1):
        if i==0 or j==0:
            arr[i][j]=0
        elif stat1[i-1]==stat2[j-1]:
            arr[i][j]=1+arr[i-1][j-1]
        else:
            arr[i][j]=max(arr[i-1][j] ,arr[i][j-1])
print(arr[m][n])
