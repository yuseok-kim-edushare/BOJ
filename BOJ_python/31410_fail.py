import sys
input=sys.stdin.readline
n=int(input())
posi=[]
for _ in range(0,n):
    posi.append(list(map(int,input().split())))
posi.sort()
lefts=0
rights=0

for j in range(0,n-1):
    lefts=lefts+posi[j][1]
    if j!=0:
        lefts=lefts+j*(posi[j][0]-posi[j-1][0])
for k in range(0,n-1):
    rights=rights+posi[n-1-k][1]
    if k!=0:
        rights=rights+k*(posi[n-k][0]-posi[n-k-1][0])
print(min(lefts,rights))
