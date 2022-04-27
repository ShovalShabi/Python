#Presentor:Shoval Shabi ID:208383885
def demand_list(lst):
    return [val if (index %2==0 and val %2!=0)or(index %2!=0 and val %2==0) else int(val/2)if index %2==0 and val %2== 0 else [val,val] for val,index in zip(lst,list(indexes for indexes in range(len(lst))))]

def remove_inner_lists(lst):
    return sum(map(lambda x:x if isinstance(x,list) else [x],lst),[])


val=demand_list([1,2,4,5,6,3,9,8])  #should return [1, 2, 2, [5, 5], 3, [3, 3], 9, 8]
print(val)
val=remove_inner_lists(val)  #should return [1, 2, 2, 5, 5, 3, 3, 3, 9, 8]
print(val)

