def getdata():
    num=int(input("enter number"))
    return num
def count(num):
    for i in range(0,num+1):
        print(i)
def main():
    num=getdata()
    count(num)
main()
        
