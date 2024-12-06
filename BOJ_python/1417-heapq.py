import sys
input=sys.stdin.readline
import heapq

n=int(input())
if n==1:
    input()
    print(0)
else:
    me = int(input())
    votes = []
    for _ in range(n - 1):
        num = int(input())
        heapq.heappush(votes, (-num, num))
#최소 힙 정렬을 -num 기준으로 돌리고 입력을 num을 하면 최대 힙이 되어요
    count = 0
    while True:
        leader = heapq.heappop(votes)[1]
        if leader >= me:
            count += 1
            me += 1
            heapq.heappush(votes, (-leader +1, leader -1))
        else:
            break
    print(count)
        
        
