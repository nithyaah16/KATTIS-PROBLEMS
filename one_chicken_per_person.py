x=input().split()

n=int(x[0])
c=int(x[1])

if n>c:
    q=n-c
    if q>1:
        print("Dr. Chaz needs {} more pieces of chicken!".format(str(q)))
    else:
        print("Dr. Chaz needs {} more piece of chicken!".format(str(q)))
else:
    q=c-n
    if q>1:
        print("Dr. Chaz will have {} pieces of chicken left over!".format(str(q)))
    else:
        print("Dr. Chaz will have {} piece of chicken left over!".format(str(q)))
