a=list(map(int,input().split()))
b=list(map(int,input().split()))
switch=0
sa=0
sb=0
for i in range(0,9):
    sa=sa+a[i]
    if sa>sb:
        switch=1
        break
    sb=sb+b[i]
if switch==1:
    print('Yes')
else:
    print("No")