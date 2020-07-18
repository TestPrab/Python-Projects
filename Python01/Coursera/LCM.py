def gcd(a,b):
    if a==0:
        return b
    elif a==b:
        return a
    else:
      return gcd(b%a,a)
n=list(map(int,input().split()))
GCD=(gcd(n[0],n[1]))
LCM=int((n[0]*n[1])//GCD)
#print(GCD)
print(LCM)
