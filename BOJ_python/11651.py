import sys
input=sys.stdin.readline
n=int(input())
p=[]
for _ in range(0,n):
    a=list(map(int,input().split()))
    a=[a[1],a[0]]
    p.append(a)
p.sort()
for i in range(0,n):
    m=str(p[i][1])+' '+str(p[i][0])
    print(m)