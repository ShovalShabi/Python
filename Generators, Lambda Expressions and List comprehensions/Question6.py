#Presentor:Shoval Shabi ID:208383885
###############################Helper function#################################
def check_div_more_than_num(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
           sum+=i
    if sum>num:
        return True
    return False
#############################Generator function################################

def func_gen(lst):
    for val in lst:
        if check_div_more_than_num(val):
            yield val
#############################Generator function in one line####################
def one_line_gen(lst):
    return filter(check_div_more_than_num,lst) #filter returns iterable over the constraint of check_div_more_than_num

#############################Generator class###################################
class MyGen:
    def __init__(self,list):
        self.list=list
        self.index=0

    def __iter__(self):
        self.index=0  #for further use of the iterable class (can be iterated over more than once)
        return self

    def __next__(self):
        while True:
            if self.index==len(self.list):
                raise StopIteration
            if self.check_div(self.list[self.index]):
                index=self.index
                self.index+=1
                return self.list[index]
            self.index+=1

    def check_div(self,num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum > num:
            return True
        return False
##############################################################################


g=func_gen([1,2,4,6,7,10,100,5,9,25,12])
print((list(g)))  #returns [100, 12]
g=one_line_gen([1,2,4,6,7,10,100,5,9,25,12])
print(list(g))  #returns [100, 12]
gen=MyGen([1, 2, 4, 6, 7, 10, 100, 5, 9, 25, 12])
print(list(gen))  #returns [100, 12]
