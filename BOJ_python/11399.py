import sys
input=sys.stdin.readline
n=int(input())
p=list(map(int,input().split()))
p.sort()
ans=0
for i in range(n):
    temp=0
    for j in range(i+1):
        temp=temp+p[j]
    ans=ans+temp
print(ans)