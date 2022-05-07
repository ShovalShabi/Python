#Presentor:Shoval Shabi ID:208383885
funcs=[]
def dec_3last_funcs(func):
    global funcs
    def wrapper():
        if len(funcs)==3:
            funcs.pop()
        funcs.insert(0,func.__name__)
        if len(funcs) >2:
            print(funcs)
    return wrapper

@dec_3last_funcs
def foo1():
    pass
@dec_3last_funcs
def foo2():
    pass

@dec_3last_funcs
def foo3():
    pass

@dec_3last_funcs
def foo4():
    pass


foo1()
foo2()
foo3()  #should print here ['foo3', 'foo2', 'foo1']
foo4()  #should print here ['foo3', 'foo2', 'foo1']
foo3()  #should print here ['foo3', 'foo4', 'foo3']
