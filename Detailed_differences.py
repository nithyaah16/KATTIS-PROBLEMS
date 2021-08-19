n=int(input())

for i in range(n):
    x=input()
    y=input()
    ans=""
    for i,j in zip(x,y):
        if i==j:
            ans=ans + "."
        else:
            ans=ans+ "*"
    print(x)
    print(y)
    print(ans)
    print('\n')
