import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000005)

#기본 입력 받기

n = int(input())

bamboos = []
for _ in range(n):
    bamboos.append(list(map(int,input().split())))


#탐색 위한 그래프 그리기 + Depth Memoization 위한 칸 만들기

depth = []
for _ in range(n):
    c = []
    for _ in range(n):
        c.append(0)
    depth.append(c)


#dfs go

def dfs(point):
    global depth
    x,y = point
    if depth[x][y] != 0:
        pass
    else:
        depth[x][y] = 1
        vertex=[]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            p = (x+dx[i], y+dy[i])
            if p[0]<n and p[1]<n and p[0]>-1 and p[1] > -1 and bamboos[p[0]][p[1]]>bamboos[x][y]:
                vertex.append(p)
        for b in vertex:
            depth[x][y] = max(depth[x][y], dfs(b)+1)
    return depth[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        a = (i,j)
        ans = max(ans, dfs(a))
print(ans)
