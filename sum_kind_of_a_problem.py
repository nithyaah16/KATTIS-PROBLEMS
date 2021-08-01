t=int(input())
        

for i in range(t):
    x=input().split()
    s=0
    su=0
    n=int(x[1])
    for i in range(1,n+1):
        s=s+i
        if i<n:
            su=su+((2*i) + 1)
    odd=su+1
    even=2*(s)
    print(int(x[0]),s,odd,even)
