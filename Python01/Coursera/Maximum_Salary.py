def decide(num,md):
    if( int(str(num)+str(md))>=int(str(md)+str(num))):
        return True
    else:
      return False
n=int(input())
arr=[]
ans=""
arr=[int(p) for p in input().split()]
answer=[]
while len(arr)>0:
    max_num=0
    for i in arr:
      if  decide(i,max_num):
          max_num=i
    answer.append(max_num)
    arr.remove(max_num)


ans="".join(str(i)for i in answer)
print(ans)



            
