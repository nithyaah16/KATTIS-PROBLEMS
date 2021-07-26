lst=[]

for i in range(10):
    x=int(input())
    mod=x%42
    if mod not in lst:
        lst.append(mod)

print(len(lst))
