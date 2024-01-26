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
