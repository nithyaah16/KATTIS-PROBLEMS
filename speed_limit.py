state=True

def foo(n):
    dic={}
    total=0
    for i in range(n):
        x=input().split()
        s=int(x[0])
        t=int(x[1])
        dic[i]=[s,t]

    for j in dic:
        if j==0:
            total=total+(dic[j][0]*dic[j][1])
        else:
            total=total+(dic[j][0]*(dic[j][1]-dic[j-1][1]))

    return total

while state==True:
    n= int(input())
    if n!=-1:
        print(foo(n),"miles")
    else:
        state=False
