import re

myl = [1,7,-2,0,4,9,1,2,5,6,2,8,3,11]
target = int(raw_input("enter the sum:::"))
for x in myl:
    if target-x in myl:
        print "here are the numbers",x,target-x,"at indexces:::",myl.index(x),myl.index(target-x)