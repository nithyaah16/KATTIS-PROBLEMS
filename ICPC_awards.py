n=int(input())
count=0
dic={}

while n!=0:
    x=input().split()
    u=x[0]
    t=x[1]
    if u not in dic.keys():
        dic[u]=[t]
        count=count+1
    else:
        dic[u].append(t)
    if len(dic)==12:
        n=0

for i,j in dic.items():
    print(i, j[0])
