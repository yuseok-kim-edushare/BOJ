import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
finding=list(map(int,input().split()))

counting={}

for x in card:
    if x in counting:
        pass
    else:
        counting[x]=1
        
write=sys.stdout.write

for y in finding:
    if y in counting:
        write(str(counting[y])+' ')
    else:
        write('0 ')