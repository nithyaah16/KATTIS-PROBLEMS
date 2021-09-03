n=int(input())
lst=[]
lst1=[]

for i in range(n):
    x=input().split()
    lst.append(int(x[0]))
    lst.append(int(x[1]))

for i in range(0,len(lst),2):
    a=lst[i]
    b=lst[i+1]
    for j in range(a,b+1):
        if j not in lst1:
            lst1.append(j)

print(len(lst1))
        
