#Presentor:Shoval Shabi ID:208383885
def composeStr(list_ch, list_num):
    return "".join(list_ch[position-1] for position in list_num)


print(composeStr(['u','y','e','f','h','a' ], [1,5,3,6,2,4]))  #will print "uheayf"


