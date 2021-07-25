x=int(input())

for i in range(x):
    bp=input().split()
    b=float(bp[0])
    p=float(bp[1])
    bpm=(b*60)/p
    y=60/p
    abpm_min=bpm-y
    abpm_max=bpm+y
    print("{:.4f}".format(abpm_min),"{:.4f}".format(bpm),"{:.4f}".format(abpm_max))