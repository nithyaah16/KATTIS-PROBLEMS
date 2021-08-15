n=int(input())

for i in range(n):
    g=int(input())
    x=input().split()
    for j in x:
        if x.count(j) !=2:
            ans=j
    print("Case #{}: {}".format(i+1,ans))
