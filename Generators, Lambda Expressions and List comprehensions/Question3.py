#Presentor:Shoval Shabi ID:208383885
from functools import reduce

def new_lst(lst):
    return [reduce(lambda x,y:x if x<y else y,list(inner_tuple[1] for inner_tuple in lst))
                for _ in range(max(inner_tuple[0] for inner_tuple in lst)+1)]


print(new_lst([(4,9), (0,2), (1,4), (3,2)]))  #will print [2, 2, 2, 2, 2]
