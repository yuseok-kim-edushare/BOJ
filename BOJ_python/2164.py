from collections import deque
n=int(input())
cards=deque()
for x in range(1,n+1):
    cards.append(x)
for y in range(0,n-1):
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])