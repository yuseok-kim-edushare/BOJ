import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import deque

m, n, h = map(int, readline().split()) #상자 가로 M칸, 세로 N칸, 높이 h 칸
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    
countDays = 0 #세고 있는 날짜 수
remaining = 0 #남은 안 익은 토마토 수

queue = deque()
for i in range(h): 
    for j in range(n): 
        for k in range(m): #범위 안에서 토마토 상태 검사
            if box[i][j][k] == 1:
                queue.append((i, j, k)) #익은 거면 bfs 큐 목록 추가
            elif box[i][j][k] == 0:
                remaining += 1 #안 익은 거 갯수 세기

dx = [0, 0, 0, 0, 1, -1] #변위 목록
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

nextqueue = deque()
# Do BFS
def bfs():
    global remaining
    global countDays
    while queue:
        z, y, x = queue.popleft() #큐에서 BFS 탐색 시
        for i in range(6):
            az, ay, ax = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= ax  <m and 0 <= ay < n and 0 <= az <h: #이동 대상 범위가 좌표 범위 안이면
                if box[az][ay][ax] == 0:
                    nextqueue.append((az,ay,ax))
                    box[az][ay][ax] = 1
                    remaining -= 1
    if nextqueue:
        queue.extend(nextqueue)
        nextqueue.clear()
        countDays += 1
    if queue: bfs()

bfs()
if remaining>0:
    countDays = -1
print(countDays)
    
