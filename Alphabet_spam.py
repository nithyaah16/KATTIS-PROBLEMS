x=input()

l=len(x)

w=x.count("_")

lc=0
uc=0
spl=0
for i in x:
    if i.islower():
        lc=lc+1
    if i.isupper():
        uc=uc+1
    if not i.isalpha() and i!="_":
        spl=spl+1


print("{:.16f}".format(w/l))
print("{:.16f}".format(lc/l))
print("{:.16f}".format(uc/l))
print("{:.16f}".format(spl/l))
