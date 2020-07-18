def binsearch(arr,id1,id2,el):
 if (id2-id1)>=0 and id2>=0:
  m=(id1+id2)//2
  if(el==arr[m]):
    return m
  elif el>arr[m]:
     id1=m+1

     return(binsearch(arr,id1,id2,el))
  elif el<arr[m]:
     id2=m-1
     return(binsearch(arr,id1,id2,el))
 else:
  return -1
  
    
lst1=[int(i) for i in input().split()]
lst2=[int(i) for i in input().split()]
a1=lst1[0]
a2=lst2[0]
lst1.remove(a1)
lst2.remove(a2)
pos=[]
first=0
last=len(lst1)-1
for i in lst2:
   pos.append(binsearch(lst1,first,last,i))
print(*pos)