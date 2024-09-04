import random
def low():
    x=int(input("enter low number:"))
    y=int(input("enter high nnumber:"))
    print(x,"  ",y)
    comp_num=random.randint(x,y)
    return comp_num
def gues():
    print("i am thinking of a  number ")
    gus=int(input("guess the number that i am thinking of....."))
    return gus
def cheack(comp_num,gus):
     while gus!=comp_num:
         gus=int(input("guess the number that i am thinking of....."))
     print("you win ")
def main():
    comp_num=low()
    gus=gues()
    cheack(comp_num,gus)
main()




