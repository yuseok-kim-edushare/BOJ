n, m = map(int, input().split()) #n 남은 일 수, m 필요 가점
s = [0] + (list(map(int,input().split()))) #일일 봉사활동 가점 목록
a, d = map(int, input().split()) #헌혈 가점 a, 헌혈 휴식기간 d

dp = [[0] * (11*n) for i in range(n*2)] #조금 넉넉히 초기화

#헌혈하지 않을 경우에 대한 DP 값 초기화
for i in range(1,n+1):
    dp[0][i] = dp[0][i-1] + s[i]

answer = n*12 #일수에 비해 충분히 큰 값으로 답 초기화

# D<= i <= N + D - 1     
for i in range(0, n//d + 1):
    for j in range(d,n+d+1):
#dp[i][j] = max(dp[i-1][j] + s[i], dp[i-d][j-1] +A)
        dp[i][j] = max(dp[i-1][j] + s[i], dp[i-d][j-1] + a)
        if dp[i][j] >= m:
            answer = min(answer, (i-1))
            
# 이러면 O(N^2)이라구요, 이제 이해가 됩니다, 전우님

if answer == n*12:
    answer = -1
print(answer)
