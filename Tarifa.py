x=int(input())
n=int(input())
unused=0

for i in range(n):
    used=int(input())
    unused=unused+(x-used)

print(unused+x)