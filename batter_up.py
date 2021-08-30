n=int(input())

x=input().split()

count=0
sum=0

for i in x:
    z=int(i)
    if z!=-1:
        count=count+1
        sum=sum+z

ans=sum/count

print(ans)
        
