n=int(input())

for i in range(n):
    x=input().split()
    if x[0]=="Simon" and x[1]=="says":
        string=""
        for i in range(2,len(x)):
            if string=="":
                string=string+x[i]
            else:
                string=string+" "+x[i]
        print(string)
        