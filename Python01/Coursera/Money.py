coins=0
def valuerem(n):
    global coins
    ret=0

    if(n>=10):
        tu=ten(n)
        coins+=tu[1]
        return valuerem(tu[0])
    elif(n<10 and n>=5):
        tu=five(n)
        coins+=tu[1]
        return valuerem(tu[0])
    else:
        tu=one(n)
        coins+=tu[1]
        ret=coins
        return(ret)
def ten(m):
    num=m//10
    r=m%10
    return (r,num)
def five(m):
    num=m//5
    r=m%5
    return (r,num)
def one(m):
    num=m//1
    r=m%1
    return (r,num)
val=int(input())
print(valuerem(val))