import math 
state = True

while state==True:
    x=input().split()

    if x==["0","0","0"]:
        state=False
        break

    else:
        r=float(x[0])
        m=int(x[1])
        c=int(x[2])

        true_area=math.pi*r*r
        exp_area=4*r*r*c/m

        print("{:.10} {:.10}".format(true_area,exp_area))
