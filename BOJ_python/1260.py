import sys
import collections
from collections import deque
input=sys.stdin.readline
n,v,start=map(int,input().split())
vertex=[0]*(n+1)
for a in range(n+1):
    vertex[a]=set([])
for i in range(v):
    x,y=map(int,input().split())
    vertex[x].add(y)
    vertex[y].add(x)
for b in range(n+1):
    vertex[b]=sorted(list(vertex[b]))
dfslist=[start]
bfslist=[start]
def dfs(idx):
    for c in vertex[idx]:
        if c not in dfslist:
            dfslist.append(c)
            dfs(c)
queue = deque()
def bfs(idx):
    queue.append(idx)
    while queue:
        temp=queue.popleft()
        for x in vertex[temp]:
            if x not in bfslist:
                queue.append(x)
                bfslist.append(x)
dfs(start)
bfs(start)
print(*dfslist)
print(*bfslist)
