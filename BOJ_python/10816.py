import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
finding=list(map(int,input().split()))

counting={}

for x in card:
    if x in counting:
        counting[x]+=1
    else:
        counting[x]=1
        
for y in finding:
    if y in counting:
        print(counting[y], end=' ')
    else:
        print('0',end=' ')
       
#sys.stdout.write 함수 쓰니까 시간이 840->752[ms]