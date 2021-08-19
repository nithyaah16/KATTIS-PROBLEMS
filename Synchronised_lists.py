state=True

while state==True:
    n=int(input())
    if n!=0:
        lst1=[]
        lst2=[]

        for i in range(1,(2*n)+1):
            if i<=n:
                x=int(input())
                lst1.append(x)
            if i>n:
                y=int(input())
                lst2.append(y)

        dic={}
        temp1=sorted(lst1)
        temp2=sorted(lst2)

        for i in range(len(temp1)):
            dic[temp1[i]]=temp2[i]
        

        for i in lst1:
            print(dic[i])
        
        print("\n")
    else:
        state=False
