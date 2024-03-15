import math
n,m = map(int,input().split())
if n==m:
    target = [n]
else:
    target = range(n,m+1)
for i in target:
    if i==1:
        pass
    else:
        ccount = 0
        t = int(math.sqrt(i))
        for j in range(2,t+1):
            if i%j==0:
                ccount=ccount+1
            if ccount==1:
                break
        if ccount==0:
            print(i)