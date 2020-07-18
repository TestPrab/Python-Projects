# python3
def majority_element(elements):
    assert len(elements) <= 10 ** 5
    flag=False
    check=False
    elements.sort()
    data=set(elements)
    data=list(data)
    data.sort()
    if(len(elements)-len(data))>=len(elements)//2:
        for i in range(len(data)-1):
            i1=elements.index(data[i])
            i2=elements.index(data[i+1])
            if(i2-i1)>len(elements)/2:
                flag=True
                return 1
                break
            elif(check==False):
                if(elements.count(data[-1])>len(elements)/2):
                  flag=True
                  return 1
                  break
                check=True
            else:
                continue
    if(flag==False):
        return 0
if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
