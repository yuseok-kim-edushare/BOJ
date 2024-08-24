import sys
from collections import deque
readline = sys.stdin.readline

n = int(readline()) #총 사람 수
x, y = map(int, readline().split()) # 촌수를 비교하고 싶은 두 대상의 번호
m = int(readline()) #총 부모자식 관계
vertex = []
for i in range(n+1):
    vertex.append([])
for i in range(m):
    a, b = map(int, readline().split())
    vertex[a].append(b)
    vertex[b].append(a)
    #각각의 점에 연결된 좌표(부모관계인 상대를 기록)
queue = deque()
queue.append(x)
#loging chon-su
chonsu = [-1] * (n+1)
chonsu[x] = 0
#start bfs from x
while queue:
    idx=queue.popleft()
    for a in vertex[idx]:
        if chonsu[a] == -1: #if chonsu didn't loged, isn't visited node
            queue.append(a)
            chonsu[a] = chonsu[idx] + 1

print(chonsu[y])
