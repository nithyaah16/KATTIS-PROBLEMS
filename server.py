z=input().split()
n=int(z[0])
t=int(z[1])

x=input().split()
sum=0
count=0

for i in x:
 
    p=int(i) 
    sum=sum+p
    if sum<=t:
        count=count+1
    else:
        break


print(count)
