x=input().split()
import math

h=int(x[0])
angle=int(x[1])

ans=h/math.sin(math.radians(angle))

print(math.ceil(ans))
    
