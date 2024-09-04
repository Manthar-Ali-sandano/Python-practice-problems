from array import *
s=array("f",[10.23,11.21,41.24,90.08,45.78])
v=int(input("enter whole number between 2 and 5"))
for i in range (2,5):
          if i :
           for i in range(0,len(s)):
                print(s[i]/v)
           print(s)
           break
          else:
             print("incorrect try again")
             v=int(input("enter valid number"))


             