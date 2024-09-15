import sys
readline = sys.stdin.readline

n = int(readline()) #개단의 갯수 입력받기
stairs = [0] * 301 #계단의 목록(각 계단의 점수)
for i in range(1, n+1):
    stairs[i] = int(readline())

scores = [0] * 301  #가능한 점수의 경우의 수 메모이제이션
if n>0:
    scores[1] = stairs[1]
if n>1:
    scores[2] = stairs[1] + stairs[2]
if n>2:
    scores[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

if n > 3:
    for i in range(4, n+1):
        scores[i] = max(scores[i -3] + stairs[i -1] + stairs[i], scores[i -2] + stairs[i])
    #i 번째 계단까지 올라가는 점수 합의 최고 값을 기록
    #i번 계단을 오르기 전 i-1번 계단을 올라왔다면, n-3번 계단도 지나왔을 겁니다.
    #i번 계단을 오르기 전 i-2번 계단을 올라왔다면, 가까운 3개 계단이 이어지면 안되는
    #문제의 조건을 고려해서 i-2번 계단만 밟고 올라온다고 가정합니다.

print(scores[n])
