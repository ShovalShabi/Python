from inspect import signature
#Presentor:Shoval Shabi ID:208383885
def one_arg_func(lst):
    return list(map(lambda func:func.__name__,filter(lambda header:len(signature(header).parameters)<2,lst)))

def foo1(x,y,z):
    pass

def foo2():
    pass

def foo3(x,y):
    pass

def foo4(x):
    pass


print(one_arg_func([foo1,foo2,foo3,foo4]))  #returns every function that receives at most 1 parameters


