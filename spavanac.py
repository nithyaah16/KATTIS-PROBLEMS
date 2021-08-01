x=input().split()

h=int(x[0])
m=int(x[1])


if m>=45:
    print(h, m-45)
elif h==0:
    q=45-m
    print(23,60-q)
elif m<45:
    q=45-m
    print(h-1, 60-q)
