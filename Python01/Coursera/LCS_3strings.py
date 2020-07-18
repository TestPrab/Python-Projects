p=int(input())
stat1=input().split()
m=len(stat1)
q=int(input())
stat2=input().split()
n=len(stat2)
r=int(input())
stat3=input().split()
o=len(stat3)
arr=[[[0 for i in range(o+1)] for j in range(n+1)]for k in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        for k in range(o+1):
            if i==0 or j==0 or k==0:
                arr[i][j][k]=0
            elif stat1[i-1]==stat2[j-1]==stat3[k-1]:
                arr[i][j][k]=1+arr[i-1][j-1][k-1]
            else:
                arr[i][j][k]=max(arr[i-1][j][k],arr[i][j-1][k],arr[i][j][k-1])
print(arr[m][n][o])