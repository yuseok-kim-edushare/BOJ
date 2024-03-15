import sys
input=sys.stdin.readline
n=int(input())
p=[]
for _ in range(0,n):
    p.append(list(map(int,input().split())))
p.sort()
for i in range(0,n):
    m=str(p[i][0])+' '+str(p[i][1])
    print(m)