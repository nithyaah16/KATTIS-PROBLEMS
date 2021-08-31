state=True
t=int(input())
lst=[]
count=0

for i in range(t):
    n=int(input())
    lst.append(n)

max=lst[len(lst)-1]

for i in range(max):
    count=count+1
    if int(count) not in lst:
        print(count)
        state=False
    
if state==True:
    print("good job")
