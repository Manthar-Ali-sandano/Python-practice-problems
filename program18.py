# x=input("enter 1st name")
# y=input("enter 2nd name")
# z=input("enter 3rd name")
# lis=[x,y,z]
# l=3
# p=input("do u want to add another Y/N")
# while p=='y':
#     s=input("enter the another name")
#     p=input("do u want to add another Y/N")
#     l=l+1
# print("total number of poepl invitd in the part is",l)

mums=[]
count=0
while count<3:
    p=input('enter the name')
    mums.append(p)
    print(mums)
n=input(('do u want tghe last number saved Y/N'))
if n=='n':
    mums.remove(n)
print(mums)