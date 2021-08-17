n=int(input())
total=0

x=input().split()
for i in x:
    if i[0]=="-":
        total=total+int(i[1:])

print(total)
        
