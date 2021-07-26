n=int(input())
count=0

for i in range(n):
    x=input()
    y=x.lower()
    if "rose" in y or "pink" in y:
        count=count+1

if count!=0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
