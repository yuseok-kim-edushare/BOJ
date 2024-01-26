t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    if n==m:
        print(1)
    else:
        ans=1
        for j in range(n+1,m+1):
            ans=ans*j
        for k in range(1,m-n+1):
            ans=ans//k
        print(ans)
# index num 이유로 range(a,b)의 b값은 의도한 값 +1을 입력해야 함
