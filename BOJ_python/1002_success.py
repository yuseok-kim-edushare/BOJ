import sys
input=sys.stdin.readline
n=int(input())
for _ in range(0,n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    L2=(x1-x2)**2+(y1-y2)**2
    rR=(r1+r2)**2
    rr=(r1-r2)**2
    if L2==0 and r1==r2:
        print(-1)
    elif rR>L2>rr:
        print(2)
    elif rR==L2 or rr==L2:
        print(1)
    else:
        print(0)
#L2 : 두 원의 중심거리의 제곱
#rR : 두 원의 중심과 떨어진 한 점의 거리 2개 합의 제곱
#rr : 거리 2개의 차이의 제곱
#제곱 사용 이유 : 제곱근은 소수로 내려가 부동소수점 정밀도 문제 등 우려, 정수형 유지하며 부호 구분을 생략하기 위해 제곱 : (-1)^2 = 1
