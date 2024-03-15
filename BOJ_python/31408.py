n=int(input())
noye=list(map(int,input().split()))
count=[0]*100001
for x in noye:
    count[x]=count[x]+1
if max(count)>((1+n)//2):
    print("NO")
else:
    print("YES")