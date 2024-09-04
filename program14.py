
mums=[]
count=0
while count<3:
    p=input('enter the name')
    mums.append(p)
    print(mums)
    count=count+1
n=input(('do u want tghe last number saved Y/N'))
if n=='n':
    mums.remove(p)
print(mums)