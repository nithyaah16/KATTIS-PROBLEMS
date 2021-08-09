n=int(input())
alphs=["a","b",'c','d','e','f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(n):
    x=input().lower()

    missing=""
    for i in range(len(alphs)):
        if alphs[i] not in x:
            missing=missing+alphs[i]
    if missing=="":
        print("pangram")
    else:
        print("missing",missing)
