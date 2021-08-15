s=int(input())

if s==1:
    print(1)
else:

    days=1
    printers=1
    while (s > printers):
        printers=printers+(2**(days-1))
        days=days+1
       

    print(days) 
