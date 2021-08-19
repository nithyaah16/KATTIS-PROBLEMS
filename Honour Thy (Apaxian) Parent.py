word=input().split() 
x=word[0]
z=word[1]
q=x[-2:]
y=x[len(x)-1]
ans=""

if y=="e":
    ans=ans+x+"x"+z
elif y in ['a','u','i','o']:
    new=x[:len(x)-1]
    ans=ans+new+"ex"+z
elif q=="ex":
    ans=ans+x+z
else:
    ans=ans+x+"ex"+z

print(ans)
