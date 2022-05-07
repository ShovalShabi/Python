import math
#Presentor:Shoval Shabi ID:208383885
#one line lambda expression that returns natural root of a number if it's an integer else returns 0
find_root=lambda x: int(math.sqrt(x)) if math.sqrt(x) %1==0 else 0

lst=[10,0,4,8,16,25,13,36]
for val in lst:
    print("for ",val," the result is:",find_root(val))
