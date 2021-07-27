x=input().split()

l=int(x[0])
r=int(x[1])

if l==r and l!=0:
    print("even ",l+r)
elif l>r:
    print("odd ",l*2)
elif l<r:
    print("odd ",r*2)
else:
    print("not a moose")
