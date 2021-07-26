x=input()

a=1
b=0
c=0

for i in x:

    if i=="A":
        a,b=b,a
    elif i=="B":
        b,c=c,b
    else:
        a,c=c,a
    if a==1:
        mark=1
    elif b==1:
        mark=2
    elif c==1:
        mark=3

print(mark)
