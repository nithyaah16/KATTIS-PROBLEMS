state = True

while state==True: 
    n=int(input())
    dic={}
    if n != 0:
        for i in range(n):
            x=input()
            if x[0:2] not in dic:
                dic[x[0:2]]=[]
                dic[x[0:2]].append(x)
            else:
                dic[x[0:2]].append(x)
        dic1=sorted(dic)
        for k in dic1:
            for words in dic[k]:
                print(words)
        print("\n")
    else:
        break
