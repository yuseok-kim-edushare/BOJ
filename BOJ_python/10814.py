import sys
input=sys.stdin.readline
n=int(input())
users=[]
for x in range(0,n):
    a=input().split()
    b=[int(a[0]),x,a[1]]
    users.append(b)
users.sort()
for k in range(0,n):
    m=str(users[k][0])+' '+users[k][2]
    print(m)