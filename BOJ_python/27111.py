import sys
input=sys.stdin.readline
n = int(input())
count = 0
usr=[0]*200002
for _ in range(0,n):
    a,b = map(int,(input().split()))
    if usr[a]==b:
        count=count+1
    else:
        usr[a]=b
count = count + usr.count(1)
print(count)