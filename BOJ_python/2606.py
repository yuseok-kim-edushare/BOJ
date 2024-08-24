import sys
readline = sys.stdin.readline

n = int(readline()) #컴퓨터 대수
v = int(readline()) #연결 쌍의 수
vertex = [] #간선 목록을 저장할거에요
for i in range(n+1):
    vertex.append([])
    
for _ in range(v):
    a, b = map(int, readline().split())
    vertex[a].append(b)
    vertex[b].append(a)
    #간선 목록을 받아서 각 정점 번호에 연결된 상대방을 기록할 거에요

infected = set([1])

def dfs(idx):
    for i in vertex[idx]:
        if i in infected:
            pass
        else:
            infected.add(i)
            dfs(i)

dfs(1)
print(len(infected)-1)
#탐색 중에 1번을 다시 방문할 수도 있으니, 미리 추가해 주었어요.
#그렇지만 1번이 감염시킨 수를 찾아야 하니, 감염된 컴퓨터 수에서 1을 빼야 해요
