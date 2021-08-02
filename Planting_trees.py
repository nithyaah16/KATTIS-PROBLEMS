n=int(input())
lst=[]
maxi=0
x=input().split() 

for i in x:
    lst.append(int(i))

lst1=sorted(lst,reverse=True)

for i in range(n):
    val=lst1[i]+(i+1)
    if val>maxi:
        maxi=val

print(maxi+1)
