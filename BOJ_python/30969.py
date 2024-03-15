import sys
input=sys.stdin.readline
n=int(input())
stand=1000
count=0
idx=-1
costcount=[0]*1001
k=0
while k<n:
    dc=input().split()
    c=int(dc[1])
    if dc[0]=='jinju':
        stand=c
        idx=k
        for x in range(c+1,1001):
            count=count+costcount[x]
    if c>stand:
        count=count+1  
    elif idx==-1:
        costcount[c]=costcount[c]+1
    k=k+1
print(stand)
print(count)