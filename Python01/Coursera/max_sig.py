n=int(input())
points=[]
i=0
cords=[]
temp=[]
for _ in range(n):
    a=[int(i) for i in input().split()]
    points.append(a)
points.sort( key=lambda p:p[1] )
while i<n:
  temp=points[i]
  while i< (n-1) and temp[1]>=points[i+1][0]:
      i+=1
  cords.append(temp[1])
  i+=1
print(len(cords))
print(*cords)


    
