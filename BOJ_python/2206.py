import sys
from collections import deque
readline = sys.stdin.readline

n, m = map(int, readline().split())
k = 1
#세로 줄 N, 가로 줄 M, 벽 통과 가능 횟수 k
maps = []
visited = []
for i in range(n):
    t = []
    for x in readline().rstrip():
        t.append(int(x))
    maps.append(t)
    temp =[]
    for j in range(m):
        temp.append([0]*(k+1))
    visited.append(temp)
visited[0][0] = [1, 0]

queue = deque()
queue.append([0,0,0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    y, x, b = queue.popleft()
    #b = 벽 부순 횟수
    for i in range(4):
        ay, ax = y + dy[i], x + dx[i]
        if 0 <= ay <n and 0 <= ax < m:
        #지도 좌표 범위 안이라면 탐색 시도
            if maps[ay][ax] == 0 and visited[ay][ax][b] == 0:
                queue.append([ay, ax, b])
                visited[ay][ax][b] = visited[y][x][b]+1
            elif maps[ay][ax] == 1 and b<k  and visited[ay][ax][b] == 0:
                queue.append([ay, ax, b+1])
                visited[ay][ax][b+1] = visited[y][x][b]+1
if max(visited[n-1][m-1]) == 0:
    print(-1)
else:
    temp=list(set(visited[n-1][m-1]))
    if 0 in temp:
        temp.remove(0)
    print(min(temp))

