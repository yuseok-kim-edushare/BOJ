import sys
readline = sys.stdin.readline

meetings = []

n = int(readline())
for _ in range(n):
    start, end = map(int,readline().split())
    duration = end-start
    meetings.append([start,end])

meetings = sorted(meetings, key = lambda x: (x[1], x[0]))

count = 0
cursor = 0

for meet in meetings:
    if cursor <= meet[0]:
        count += 1
        cursor = meet[1]
        
print(count)
