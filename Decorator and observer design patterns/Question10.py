#Presentor:Shoval Shabi ID:208383885
####################################################################
#wrapped_func_use is dictionary destined for the summoned functions
#str- destined for the name of the function
#list- number of summons of specific function placed in index 0, number of
#keywords and positionals that specif function got so far placed in index 1
###########################################################################
wrapped_func_use={str:list}
returned_types_dict={'Int':0,'Float':0,'Bool':0,'Str':0,'List':0,'Set':0,'Dict':0,'Tuple':0}
total_use=0  #The total use of wrapped functions
def dec_call_statistics(func):
    global returned_types_dict

    #Helper method for checking several types of variables
    def classify_types(returned_val):
        global  returned_types_dict
        if isinstance(returned_val,int):
            returned_types_dict['Int']+=1
        if isinstance(returned_val,float):
            returned_types_dict['Float']+=1
        if isinstance(returned_val,bool):
            returned_types_dict['Bool']+=1
        if isinstance(returned_val,str):
            returned_types_dict['Str']+=1
        if isinstance(returned_val,list):
            returned_types_dict['List']+=1
        if isinstance(returned_val,set):
            returned_types_dict['Set']+=1
        if isinstance(returned_val,dict):
            returned_types_dict['Dict']+=1
        if isinstance(returned_val,tuple):
            returned_types_dict['Tuple']+=1

    def wrapper(*args,**kwargs):
        global total_use
        global wrapped_func_use
        total_use += 1
        if func.__name__ not in wrapped_func_use:
            wrapped_func_use[func.__name__]=[0,0]
        wrapped_func_use[func.__name__][0]+=1
        wrapped_func_use[func.__name__][1]+=len(args)+len(kwargs)
        returned_val=func(*args,**kwargs)
        classify_types(returned_val)
        print(f'the function {func.__name__} summoned {wrapped_func_use[func.__name__][0]} times and used {wrapped_func_use[func.__name__][1]} variables neither positionals or keywords')
        print(f'Total use of the decorator is {total_use} times and the types that returned by any function are:{returned_types_dict}')
        print()


    return wrapper
#################################################Basic functions########################################################
@dec_call_statistics
def func1(*args,**kwargs):
    return args[0]

@dec_call_statistics
def func2(*args,**kwargs):
    return kwargs

@dec_call_statistics
def func3(*args,**kwargs):
    return sum(args)

@dec_call_statistics
def func4(*args,**kwargs):
    return args[0]/20


func1(1,2,4,z=8)
func2('hey','bye',a=5,b=6,c=7)
func3()
func4(4.5,20,3,hey='bye')
func1('hey')
func1((0,1,2,9),5)
func1(True)
func3()



