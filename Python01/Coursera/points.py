s,p=[int(i) for i in input().split()]
cords=[]
frequency=0
freq={}
for i in range(s):
    a,b=[int(i) for i in input().split()]
    cords.append([a,"l"])
    cords.append([b,"r"])
point=[int(i) for i in input().split()]
for i in range(p):
    a=point[i]
    cords.append([a,"p"])
cords.sort()
for i in cords:
    a=i[1]
    if a=="l":
        frequency+=1
    elif a=="r":
        frequency-=1
    else:
        freq[i[0]]=frequency
temp=""
for i in point:
    temp += str(freq[int(i)]) + ' '
print(temp[:-1])


