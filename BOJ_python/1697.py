from collections import deque
n, k = map(int, input().split())
#출발 위치 좌표 n, 목적지 좌표 k
posi = [-1] * 200010
#각 좌표 별 방문에 소요된 시간 체크할 목록
queue = deque()
queue.append(n)
#n 부터 탐색 시작할 거에요
while queue:
#bfs 위한 반복문(큐가 안 비었음 계속 탐색)
    if posi[k] == -1:
    #만약 목적지 도달 못 했다면
       x = queue.popleft()
       tar = [x-1, x+1, x*2]
    #각각 1초가 걸리는 앞, 뒤,
    #순간이동 시 도착 좌표
       for i in tar:
           if i < 100002 and i > -1:
     #음수 및 지나친 먼 좌표는 없어야 해서 필터
               if posi[i] == -1:
       #i가 탐색된 적 없는 좌표면
                   posi[i] = posi[x] + 1
                   queue.append(i)
    else:
        queue = deque()
        #만약 목적지까지 탐색 했음 큐 초기화
print(posi[k])
