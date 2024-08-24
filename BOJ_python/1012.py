import sys
from collections import deque
readline = sys.stdin.readline
sys.setrecursionlimit(1000000)

queue = deque()
def bfs(pos): #배추 좌표에서 출발하는 BFS 함수
    queue.append(pos)
    #t_visit = set() #이번 회차 bfs의 방문 리스트
    while queue:
        temp=queue.popleft()
        ways = [(temp[0] + 1, temp[1]),
                (temp[0] - 1, temp[1]),
                (temp[0], temp[1] + 1),
                (temp[0], temp[1] - 1)]
        #방문할 방향들을 확인해요.
        for a in ways:
            if a in positions: #그 점에 배추가 있는지 볼거에요.
                if a in visited:
                    pass
                else:
                    queue.append(a)
                    visited.add(a)

t = int(readline()) #test case 수
for i in range(t):
    M, N, K = map(int,readline().split())
    #배추 밭 가로, 세로, 심어진 배추 수 M,N,K
    if K == 1:
        print(1) #생각해보니 배추 1개면 탐색도 필요 없네요
    else:
        positions = [] #배추가 있는 좌표들을 저장해요
        visited = set()
        for j in range(K):
            positions.append(tuple(map(int, readline().split())))
            #좌표 입력받아서 보관할 거에요
        count = 0 # 세야 할 카운트에요. (연결된 배추 집단이 몇 개인가)
        for x in positions:
            if x not in visited:
                visited.add(x)
                bfs(x)
                count += 1
        if len(positions) == len(visited):
            print(count)
