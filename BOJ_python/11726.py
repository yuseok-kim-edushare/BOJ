n = int(input()) #2xn 타일링의 n 입력

count = [0] * 1002
count[1] = 1 # 2X1 이면 2*1 타일 1개의 1가지
count[2] = 2 # 2X2 이면 1*2 타일 2개 혹은 2*1타일 2개의 2가지
count[9] = 55 #주어진 테케

for i in range(1,n+1):
    if count[i] != 0:
        pass
    else:
        count[i] = (count[i-1] + count[i-2]) %10007 #답은 %10007 한 값 출력하랬음
        #옆으로 1*2타일 2개 늘리거나 (i-2에서)
        #옆으로 2*1 타일 1개 늘리거나(i-1에서)

print(count[n])
