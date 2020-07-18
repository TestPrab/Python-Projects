W,n=[int(i) for i in input().split()]
content=list(map(int,input().split()))
arr=[[0 for row in range(W+1)] for col in range(n+1)]
for i in range(n+1):
    for w in range(W+1):
        if i==0 or w==0:
            arr[i][w]=0
        elif content[i-1]<=w:
            arr[i][w]=max(arr[i-1][w],arr[i-1][w-content[i-1]]+content[i-1])
        else:
            arr[i][w]=arr[i-1][w]
print(arr[n][W])