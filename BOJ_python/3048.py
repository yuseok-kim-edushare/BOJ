n1, n2 = map(int, input().split()) #n1, n2 각 그룹의 개미 수
rightAnts = list(input())
rightAnts.reverse()
leftAnts = list(input())
t = int(input())

if t == 0:
    answer = rightAnts + leftAnts
elif t in range(1, n1+n2):
    table = []
    for x in rightAnts:
        table.append((x,1))
    for x in leftAnts:
        table.append((x,0))
    for i in range(t):
        shadows = list(table)
        for j in range(n1+n2-1):
            if table[j][1] == 1 and table[j+1][1] == 0:
                shadows[j], shadows[j+1] = shadows[j+1], shadows[j]
        table = list(shadows)
    answer =[]
    for x in table:
        answer.append(x[0])
else:
    answer = leftAnts + rightAnts
print(*answer, sep='')
