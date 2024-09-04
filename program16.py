from array import *
s=array('i',[1,1,2,4,0])
x=int(input("enter number from array"))
count=0
for i in s:
    print(i)
    if i==x:
       count=count+1
print(x,"is",count,"times repeated") 