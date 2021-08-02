state=True
while state==True:

    x=input().split()

    if x==["0","0"]:
        state=False
        
    else:
        a=int(x[0])
        b=int(x[1])
 
        w=a//b
        n=a%b

        print(w,n,"/",b)
