n=int(input())
pep=[]
for _ in range(n):
    pep.append(list(map(int,input().split())))
rank=[1]*n
for a in range(0,n-1):
    for b in range(a+1,n):
        if pep[a][0]>pep[b][0]:
            if pep[a][1]>pep[b][1]:
                rank[b]=rank[b]+1
        elif pep[a][0]<pep[b][0]:
            if pep[a][1]<pep[b][1]:
                rank[a]=rank[a]+1
for x in rank:
    print(x,end=' ')