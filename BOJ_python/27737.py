import sys
from collections import deque

readline = sys.stdin.readline
queue = deque()
def bfs(pos): #좌표에서 출발하는 BFS 함수
    queue.append(pos)
    count = 1 # 몇 칸이 이어져 있는 지 확인해요
    while queue:
        temp=queue.popleft()
        ways = [(temp[0] + 1, temp[1]),
                (temp[0] - 1, temp[1]),
                (temp[0], temp[1] + 1),
                (temp[0], temp[1] - 1)]
        #방문할 방향들을 확인해요.
        for a in ways:
            if a[0] not in range(N) or a[1] not in range(N):
                pass
            elif woods[a[0]][a[1]] == 0:#나무판 상태를 확인해요
                if a in visited:
                    pass
                else:
                    queue.append(a)
                    visited.add(a)
                    count += 1
    return count #이어진 범위를 다 짚으면 모두 몇 개인지 반환해요

N, M, K = map(int, readline().split())
#N*N 나무판의 크기 / M 포자 수, K 포자의 확산 가능 거리
woods = []
for _ in range(N):     #나무판 상태 기록
    woods.append(list(map(int, readline().split())))
    
visited = set()
m = M #현재 남은 포자수 m

for x in range(N):
    for y in range(N):
        if woods[x][y] == 0: #아! 나무판 검사하고, 괜찮은 칸인데 왜 안 심어졌지를 봐야지...
            if (x, y) not in visited:
                visited.add((x, y))
                blocks = bfs((x, y)) #bfs 통해서 몇 칸이나 채워야 하는 지 추적
                m -= blocks // K #1개 포자 당 k개 칸을 채우니 우선 칸수를 k로 나눈 몫을 빼 주고
                if blocks % K != 0: #나머지가 있으면 한개 더 사용해야 하는 거 반영
                    m -= 1

if m == M or m < 0: #포자를 못 썼거나, 포자가 모자라면 불가능
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m)
