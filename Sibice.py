x=input().split()
n=int(x[0])
w=int(x[1])
h=int(x[2])

for i in range(n):
    l=int(input())
    if ((w*w) + (h*h)) >= l*l:
        print("DA")
    else:
        print("NE")
