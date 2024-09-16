n, m = map(int, input().split()) #n 남은 일 수, m 필요 가점

s = [0]
s.extend(list(map(int,input().split()))) #일일 봉사활동 가점 목록

a, d = map(int, input().split()) #헌혈 가점 a, 헌혈 휴식기간 d

s.extend([0]*(d-1))
maxGiving = (len(s)+d-1)//d+1
#최대 헌혈 가능 횟수: (d+1)일 당 1회 가능, 근사치 사용

dp = [[0] * (maxGiving) for i in range(len(s))] #dp memoization
#dp[현재 날짜][헌혈 횟수] 구조임

for i in range(len(s)): #날짜를 지나보내는 반복문 구문 실행
    #i일까지의 결과 = 휴식기간이 고려되었음, n일 헌혈 후 휴식 결과까지 추적
    dp[i][0] = dp[i-1][0] + s[i]
    #매일 매일 봉사활동 점수만 누적했음
    #헌혈하지 않을 경우에 대한 DP 값 초기화
    if i >= d: #첫 휴식기간부터 지나가면 헌혈의 경우 고려 필요
        for j in range(1, maxGiving):
            dp[i][j] = max(dp[i-1][j] + s[i], dp[i-d][j-1] +a)
            #전날에 이어 봉사활동 하는 게 유리한지, 헌혈하는 게 유리한지 계산

for count in range(len(dp[-1])): #마지막 날의 점수 결과 비교
    if dp[-1][count] >= m: #헌혈 0회부터 차례로 세어서, 합격 가능하면
        print(count) #가능한 최소의 헌혈횟수니 출력하고 종료
        break
else:
    print(-1) #출력하지 못 했으면 실패니 -1 출력
print(dp)
