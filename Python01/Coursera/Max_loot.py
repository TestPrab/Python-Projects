n,W=input().split()
n=int(n)
W=int(W)
arr=[]
total_val=0
for i in range(n):
    v,w=[int(p) for p in input().split()]
    arr.append([v,w])

arr.sort(key = lambda p: p[0]/p[1], reverse = True)
for v,w in arr:
    if W==0:
        print ('%.4f'%total_val)
        break
    else:
        a=min(w,W)
        total_val+=a*(v/w)
        w=w-a
        W=W-a
print('%0.4f'%total_val)
