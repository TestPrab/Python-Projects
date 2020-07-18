def period(m):
  first=0
  second=1
  temp=0
  for i in range(0,m*m):
    temp=second
    second=(first+second)%m
    first=temp
    if first==0 and second==1:
       return(i+1)
def Fib(n,u):
  number=period(u)
  r=n%number
  lis=[0,1]
  for i in range(0,r+1):
     fib=lis[-2]+lis[-1]
     lis.append(fib)
  return(lis[-3]%u)

       
arr=list(map(int,input().split()))
print(Fib(arr[0],arr[1]))
