state=True
count=0

while state==True:
    n=int(input())
    if n==0:
        state=False
        break
    else:
        count=count+1
        lst1 = []
        lst2 = []
        for i in range(1,n+1):
            x=input()
            if i%2!=0:
                lst1.append(x)
            else:
                lst2.append(x)
        lst2.reverse()
        print("SET",count)
        for i in lst1:
            print(i)
        for j in lst2:
            print(j)
