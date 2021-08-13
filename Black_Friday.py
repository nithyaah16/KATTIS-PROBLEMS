n=int(input())
dic={}
lst=[]

x=input().split()

for i in range(n): 
    if x[i] not in dic:
        dic[x[i]]=1
    else:
        dic[x[i]]=dic[x[i]]+1


for i in dic.keys():
    if dic[i]==1:
        num=int(i)
        lst.append(num)
  

if len(lst)==0:
    print("none")
else:
    ans=max(lst) 
    print((x.index(str(ans))) + 1)
