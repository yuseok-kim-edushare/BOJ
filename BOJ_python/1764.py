import sys
input=sys.stdin.readline
n,m=map(int,input().split())
unheard=set()
unhs=set()
for i in range(n):
    unheard.add(input().rstrip())
for j in range(m):
    temp=input().rstrip()
    if temp in unheard:
        unhs.add(temp)
unhs=sorted(list(unhs))
print(len(unhs))
for x in unhs:
    print(x)