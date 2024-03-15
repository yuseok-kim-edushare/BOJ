import sys
n = int(sys.stdin.readline().rstrip())
if n==0:
    print(0)
elif n<4:
    summation=0
    for i in range(0,n):
        summation=summation+int(sys.stdin.readline().rstrip())
    print(int(0.5+summation/n))
else:
    rates=[]
    s=0
    for i in range(0,n):
        rates.append(int(sys.stdin.readline().rstrip()))
    s=int(0.5+n*0.15)
    rates.sort()
    rates=rates[s:-s]
    print(int(0.5+(sum(rates)/(n-2*s))))
#list negative index로 오른끝 잡으면 그냥 되는 거였네;;;