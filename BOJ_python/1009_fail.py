t=int(input())
for x in range(0,t):
    a,b=map(int,input().split())
    p=0
    if a==0:
        print(10)
    elif a==1:
        print(1)
    else:
        p=(a%10)**b
        print(p%10)
#시간초과 : 그래서 경우의 수 더 나눠서 구현하였더니 성공
