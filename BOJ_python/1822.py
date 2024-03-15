input()
a=set(map(int,input().split()))
b=set(map(int,input().split()))
ans=a-b
ans0=len(ans)
if ans0==0:
    print(0)
else:
    print(ans0)
    ans=list(ans)
    ans.sort()
    print(*ans,sep=' ')