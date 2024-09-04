a=[[1,2,3],[4,3,2],[4,5,6],[7,6,5]]
x=int(input(".....enter any row from above...."))
print(a[x])
y=int(input("..enter the column you want to show on that column.."))
print(a[x][y])
c=input("do u want to change the value   Y/N")
if c=='y':
    v=int(input("enter the new value"))
    a[x][y]=v
print(a[x])



