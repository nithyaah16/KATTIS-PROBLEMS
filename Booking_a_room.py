import random
nr=input().split()
n=int(nr[0])
r=int(nr[1])

if n==r:
    print("too late")
else:
    lst=[]
    state=True

    for i in range(r):
        x=int(input())
        lst.append(x)

    while state==True:
        num=random.randint(1,n)
        if num not in lst:
            print(num)
            state=False
            break
