n=int(input())

s=bin(n).replace("0b", "")

new=""

for i in range(len(s)-1,-1,-1):
    new=new+s[i]

print(int(new,2))
