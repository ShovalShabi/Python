#Presentor:Shoval Shabi ID:208383885
#########################################################Average Decorator function#####################################
sum_io=(0,0)  #0-sum of average input, 1-sum of average output
tup_avg=(0,0)
count_call_to_dec=1
def dec_avg_input_output(func):
    def wrapper(*args,**kwargs):
        global tup_avg
        global count_call_to_dec
        global sum_io
        sum_in=0
        for val in args:
            sum_in+=val
        for key in kwargs.keys():
            sum_in+=kwargs[key]
        sum_out = func(*args, **kwargs)
        sum_io=(sum_io[0]+sum_in,sum_io[1]+sum_out)
        tup_avg=(sum_io[0]/count_call_to_dec,sum_io[1]/count_call_to_dec)
        print("the average input is:",tup_avg[0]," and average output is:",tup_avg[1])
        count_call_to_dec+=1
    return wrapper

###################################################Log Decorator function###############################################
log = {str:tuple} # defining log that will store the header of each function and its return value
def dec_log(func):
    def wrapper(*args,**kwargs):
        global log
        parameters=[]
        for tupvar in args:
            parameters.append(tupvar)
        for dictvar in kwargs:
            strs=dictvar+'='+str(kwargs[dictvar])
            parameters.append(strs.replace("'",""))
        header=str(func.__name__)+str(tuple(parameters))
        log[header]=(func(*args,**kwargs))
        print("you called ",header," and it returned:",log[header])
    return wrapper

####################################################Functions of part A of the question#################################
@dec_avg_input_output
def foo1(x):
    return x

@dec_avg_input_output
def foo2(y):
    return -y

@dec_avg_input_output
def foo3(z):
    return z*z

@dec_avg_input_output
def foo4(w):
    return w-1
####################################################Functions of part B of the question#################################
@dec_log
def func1(x,y,z):
    return x+y+z

@dec_log
def func2(*args):
    sum_var=0
    for i in args:
        if i%2==0:
            sum_var+=i
        else:
            sum_var-=i
    return sum_var

@dec_log
def func3(x,y):
    return x-y

@dec_log
def func4(x,y,z):
    return x+y-z


foo1(4)
foo2(10)
foo3(7)
foo4(15)
func1(4,5,z=6)
func2(1,10,9,6)
func3(2,7)
func4(1,15,3)
