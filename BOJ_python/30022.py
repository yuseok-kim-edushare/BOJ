# TL  = 1s, ML = 1GB

import sys
readline = sys.stdin.readline

n, a, b = map(int, readline().split())
prices = []
for _ in range(n):
    p, q = map(int, readline().split())
    prices.append([(p - q), p ,q])
prices.sort()
answer =  0
for i in range(a):
    answer += prices[i][1]
for j in range(a,n):
    answer += prices[j][2]
print(answer)
