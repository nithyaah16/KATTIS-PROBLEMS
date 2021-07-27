l1=[]
l2=[]


for i in range(1,4):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    l1.append(a)
    l2.append(b)

for i in range(3):
    if l1.count(l1[i])!=2:
        x=l1[i]
    if l2.count(l2[i])!=2:
        y=l2[i]


print(x,y)
