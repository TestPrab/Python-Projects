from math import inf
num=int(input())
ops=[0]*(num+1)
for i in range(2,num+1):
    count1,count2,count3=[inf]*3
    count1=ops[i-1]+1
    if i%2==0:
        count2=ops[i//2]+1
    if i%3==0:
        count3=ops[i//3]+1
    ops[i]=min(count1,count2,count3)
    
print(ops[num])
seq=[]
n=num
while n>0:
    seq.append(n)
    if n%2!=0 and n%3!=0:
        n=n-1
    elif n%2==0 and n%3==0:
        n=n//3
    elif n%2==0:
        if ops[n-1]<ops[n//2]:
            n=n-1
        else:
            n=n//2
    else:
        if ops[n-1]<ops[n//3]:
            n=n-1
        else:
            n=n//3
print(*seq[::-1])