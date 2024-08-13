#TL 2s ML 512MB

import sys
readline = sys.stdin.readline

# n, m <= 10^6
N, M = map(int, readline().split())
road = list(map(int, readline().split()))
target = road
isCleanerOn = False
cleaner = 0
for i in range(N):
    if isCleanerOn:
        if road[i] == 0:
            isCleanerOn = False
    else:
        if road[i] == 1 :
            isCleanerOn = True
            cleaner += 1
for i in range(M):
    operation = readline().split()
    if operation[0] == "1":
        newContaIdx = int(operation[1]) - 1
        if road[newContaIdx] == 0:
            road[newContaIdx] = 1
            if newContaIdx == 0:
                if road[newContaIdx + 1] != 1:
                    cleaner += 1
            elif newContaIdx == N - 1:
                if road[newContaidx - 1] != 1:
                    cleaner += 1
            else:
                sw1 = (road[newContaIdx + 1] == 1)
                sw2 = (road[newContaIdx - 1] == 1)
                if sw1 and sw2:
                    cleaner -= 1
                elif not sw1 and not sw2:
                    cleaner += 1
    else:
        print(cleaner)
