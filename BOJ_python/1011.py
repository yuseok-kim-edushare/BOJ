t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    d=y-x
    i=1
    temp=1
    while d>temp:
        i=i+1
        temp=temp+i//2+i%2 #엔진이 이동 횟수당 갈 수 있는 최대 거리는 i번 운행시 (i를 2로 나눈 몫+2로 나눈 나머지) 만큼 증가함
    print(i)

#위 방법은 1136ms, 31120KB
#아래 방법은 40ms, 33240KB
#계산을 해 보면 위 방법이 아래 형태로 정리 가능함. JAVA로 동일 문제 풀이 하다가 TE로 인해 최적화에 대해 고민하였음

import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    d=y-x
    num=int(d**0.5)
    if num==d**0.5:
        ans=num*2-1
    elif d<=num**2+num:
        ans=num*2
    else:
        ans=num*2+1
    print(ans)
