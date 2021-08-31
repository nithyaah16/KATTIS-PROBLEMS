n=int(input())

x=input().split()
lst=[]

for i in x:
    lst.append(int(i))

min=min(lst)

print(lst.index(min))


    
        
