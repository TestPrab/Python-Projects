n=int(input())
a=[int(i) for i in input().strip().split()]
b=[int(i) for i in input().strip().split()]
a.sort()
b.sort()
summation=0
for i in range (n):
    summation+=a[i]*b[i]
print(summation)


