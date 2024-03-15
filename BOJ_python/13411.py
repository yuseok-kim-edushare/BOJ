import sys
input=sys.stdin.readline
n=int(input())
kills=[[0,0]]*n
for i in range(0,n):
    x,y,v=map(int,input().split())
    r=(x**2+y**2)**(0.5)
    kills[i]=[r/v,i+1]
kills.sort()
for y in range(0,n):
    print(kills[y][1])
#최초 정답 판정 후 수정을 통해 340ms -> 332ms로 시간 단축됨
# r2=(x**2+y**2)
# kills[i]=[r2/v/v,i+1] : 정수로만 연산하도록 거리를 구하기 위한 제곱근 연산 대신 거리 제곱을 속도록 2회 나눔
# 근데 수정한 코드를 pypy3에 그대로 넣고 돌리니 356ms에 메모리 사용량이 3배가 됨;;