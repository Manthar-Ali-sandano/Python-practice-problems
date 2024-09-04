import random

def add(num1):
    if num1==1:
      x=int(input(random.randint(5,20)))
      y=int(input(random.randint(5,20)))
      gues=int(input("you think"))
      actual=x+y
      total=(gues,actual)
    return total
def sub(num2):
    if num2==2:
      x2=int(input(random.randint(5,20)))
      y2=int(input(random.randint(5,20)))
      gues1=int(input("you think"))
      actual1=x2-y2
      total1=(gues1,actual1)
    return total1
def cheack(actual,actual1,gues,gues1):
   if actual==gues or actual1==gues1:
      print("correct")
   else:
      print("sorry")
def main():
   num1,num2,num3=menu()
   gues,actual,total=add()
   x2,y2,gues1,actual1,total1=sub()
   cheack(actual,actual1,gues,gues1)
main()
    
   








