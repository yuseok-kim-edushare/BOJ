#TL 1s ML 128MB

import math
import sys
readline = sys.stdin.readline

# n <= 10^5
n = int(readline())
positions = []
for _ in range(n):
    positions.append(int(readline()))
positions.sort()
deltas = []
for i in range(1,n):
    deltas.append(positions[i]-positions[i-1])
commonDistance = math.gcd(*deltas)
count = 0
for x in deltas:
    count += (x//commonDistance-1)
print(count)
