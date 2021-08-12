n=int(input())


for i in range(n):
    state=True
    sounds=input().split()
    dic={}
    while state==True:
        x=input().split() 
        if x== ["what","does","the","fox","say?"]:
            state=False
            break
        else:
            if x[2] not in dic.values():
                dic[x[0]]=x[2]
    for i in dic.values():
        if sounds.count(i)>0:
            while i in sounds:
                sounds.remove(i)
    ans=""
    for i in range(len(sounds)):
        if i==0:
            ans=ans+sounds[i]
        else:
            ans=ans+" "+sounds[i]
    print(ans)
