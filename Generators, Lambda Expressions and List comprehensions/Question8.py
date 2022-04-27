def funcA(m, n):
    if m < n:
        return lambda:funcA(m+1,n-1)
    elif m == n:
        return lambda:print("m==n")
    else:
        return lambda:print(m) if n <=0 else funcA(m+n,n-n)


funcA(3,10)()()()()()()  #should print 13
funcA(3,7)()()()  #should print m==n
funcA(4,4)()  #should print m==n
funcA(10, 5)()()  #should print 15
funcA(9, 5)()()  #should print 14
