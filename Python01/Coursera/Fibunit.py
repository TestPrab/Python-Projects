#last digit of a fibonnaci number
def fibl(n):
  
    lis=[0,1]
    for i in range(0,n+1):
          fib=lis[-1]+lis[-2]
          ld=fib%10
          lis.append(ld)
    return lis[-3]
n=int(input())
print(fibl(n))
