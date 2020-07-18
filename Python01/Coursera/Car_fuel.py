D=int(input())
L=int(input())
n=int(input())
points=list(map(int,input().split()))
points.append(D)
last_stop=0
current_stop=0
count=0
flag=0
while(current_stop<=n-1):
    
    last_stop=current_stop
    if(points[-1]-points[0]<=L):
        count=0
        break
    else:
       while( current_stop<=(n-1) and (points[current_stop+1]-points[last_stop])<=L) :  
            current_stop+=1 
           
       if current_stop==last_stop :
    
           flag=1
           break
       if current_stop<=n:
        
          count+=1
if (count>=0) and (flag!=1 ):
    print(count)
else:
    print("-1")

