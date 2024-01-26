import sys
input=sys.stdin.readline
n=int(input())
for _ in range(0,n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    raider1=[]
    c=0
    if x1==x2 and y1==y2 and r1+r2==0:
        print(-1)
    for xt1 in range(x1-r1,x1+r1):
        for yt1 in range(y1-r1,y1+r1):
            if ((xt1-x1)**2)+((yt1-y1)**2)-(r1*r1)<=0:
                raider1.append([xt1,yt1])
    for xt2 in range(x2-r2,x2+r2):
        for yt2 in range(y2-r2,y2+r2):
            if ((xt2-x2)**2)+((yt2-y2)**2)-(r2*r2)<=0:
                if [xt2,yt2] in raider1:
                    c=c+1
    print(c)
#BF 로 풀이 시도 : 원점 1에서 거리 안의 모든 정수 좌표 추적 + 원점 2에서 거리 안의 모든 정수 좌표 중 1번 탐지 범위 안에 있는 거 찾기
#그래서 메모리 초과, 시간 초과
