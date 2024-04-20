import sys
input=sys.stdin.readline
n,m=map(int,input().split())
pwlist=dict()
for i in range(n):
    a,b=input().split()
    pwlist[a]=b
for j in range(m):
    print(pwlist[input().rstrip()])