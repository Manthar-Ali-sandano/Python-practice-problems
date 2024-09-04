from  array import *
import random
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
x=array('i',[a,b,c])
y=array('i',[])
while len(y):
    y = random.randint(1, 5)

z=x+y
z=sorted(z)
for i in z:
    print(i)


    
