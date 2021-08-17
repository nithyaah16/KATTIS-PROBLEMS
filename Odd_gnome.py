n=int(input())

for i in range(n):
    lst=input().split()

    ans=[]

    for j in range(len(lst)-1):
        if j!=0:
            if int(lst[j])+1!=int(lst[j+1]):
                ans.append(j)

    print(ans[1])
            
           
