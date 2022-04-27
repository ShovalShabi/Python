def func(n):
    l=[]
    for i in range(n):
        j=0
        while j<i:
            if j%2 == 0:
                l.append(j+5)
            elif j % 3 == 0:
                l.append(j // 2)
            elif j%5 == 2:
                l.append(j)
            j+=1
    return l

def func_on_demand(n):
    l=sum(map(lambda x:list(map(lambda y:y+5 if y%2==0 else(y//2 if y%3==0 else(y if y%5==2 else [])),list(range(x)))),list(range(n))),[])
    return list(filter(lambda x:x!=[],l))


print(func(5))
print(func_on_demand(5))  #my implementation
