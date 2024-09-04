import os
def add():
    name=input("enter name: ")
    list.append(name)
    print(list)
    print('name added succesfully')
    return list
def change_name():
    num=0
def delete(list):
    num1=(input("which name do u wnat to delete?"))
    del list[num1]
def view():
    l=len(list)
    for i in range(0,l):
        print(i)

def exi ():
     os._exit(0)
def main():
    print("1.Add a name to the list")
    print("2.Delete name from list")
    print("3.change thae name from list")
    print("4.View all the name from list")
    print("5.exit")
    selection=int(input("select option"))
    # d=input("do u want to continue it y/N...?")
    # while d=='y':
    # print("1.Add a name to the list")
    # print("2.Delete name from list")
    # print("3.change thae name from list")
    # print("4.View all the name from list")
    # print("5.exit")
    if selection==1:
        name=add()  
        
    if selection==2:
      num1=delete()        
    if selection==3:
        num,name=add()
    if selection==4:
        l=view()

    d=input("do u want to continue it y/N...?")
    if(d=='y'):
        main()

    

list=[]
main()