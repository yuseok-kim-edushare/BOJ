import sys, heapq
readline = sys.stdin.readline

#시작 시간 순 정렬된 n개의 강의 목록 생성
lectures = []
n = int(readline())
for _ in range(n):
    start, end = map(int,readline().split())
    lectures.append([start,end])
lectures = sorted(lectures, key = lambda x:x[0])

classroom = []

for lecture in lectures:
    start = lecture[0]
    if classroom and classroom[0] <= start: 
        heapq.heappop(classroom)
    #종료 시간 기준 최소 heapq
    finish = lecture[1]
    heapq.heappush(classroom,finish)
    
print(len(classroom))
