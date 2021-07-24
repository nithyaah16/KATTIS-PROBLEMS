x=input().split(";")
count=0


for string in x:
    if "-" not in string:
        count=count+1
    else:
        nums=string.split("-")
        a=int(nums[0])
        b=int(nums[1])
        z=b-a+1
        count=count+z
        
print(count)