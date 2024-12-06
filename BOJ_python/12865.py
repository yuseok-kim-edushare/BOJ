import sys
readline = sys.stdin.readline

items = []

n, k = map(int,readline().split()) #n(물품 수), k(버틸 수 있는 무게 최댓값)
for _ in range(n):
    items.append(list(map(int, readline().split()))) #w(무게), v(가치) 입력 받기

values = [0] * (k+1)
for i in range(n):
    w, v = items[i]
    #마지막 인덱스에서 해당 물건 무게까지 역순으로 추적
    for j in range(k, w-1, -1):
        # 현재 무게에서 최대 가치와
        #해당 물건의 무게를 뺀 무게에서 가치를 더한 가치 확인
        values[j] = max(values[j], values[j-w] + v)

print(values[k])
