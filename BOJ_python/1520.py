import sys
sys.setrecursionlimit(30000)
readline = sys.stdin.readline

n, m = map(int, readline().split())

maps = []
counts = [[-1] * m for _ in range(n)]
for i in range(n):
    maps.append(list(map(int,readline().split())))
counts[0][0]  = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
        
def dfs(x, y):
    if counts[x][y]  != -1:
        pass
    else:
        counts[x][y] = 0
        for idx in range(4):
            new_x = x + dx[idx]
            new_y = y + dy[idx]
            
            if new_x<n and new_y<m and new_x>-1 and new_y>-1:
                if maps[new_x][new_y] > maps[x][y]:
                    counts[x][y] += dfs(new_x, new_y)
                    
    return counts[x][y]

dfs(n-1, m-1)
print(counts[n-1][m-1])

