#Presentor:Shoval Shabi ID:208383885
def funcB(n):
    if n == 0:
        print("the end")
    else:
        return lambda: funcB(n - 1)


funcB(5)()()()()()
funcB(3)()()()
funcB(8)()()()()()()()()