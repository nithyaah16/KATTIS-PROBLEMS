x=input().split()
lst=[]
state= True

for i in x:
    i=int(i)
    lst.append(i)


while state==True:
    for i in range(len(lst)-1): 
        a=lst[i]
        b=lst[i+1]
        if lst[i]>lst[i+1]:
            lst[i]=b
            lst[i+1]=a
            ans=""
            for j in lst:
                ans=ans+str(j)+" "
            print(ans)
            if lst==sorted(lst):
                state=False
