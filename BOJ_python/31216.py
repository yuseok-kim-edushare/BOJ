import sys
input=sys.stdin.readline
t=int(input())
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]
x=43
while x<318138:
    temp = int(x**0.6)
    for i in range(2,temp):
        if x%i==0:
            x=x+2
            break
        else:
            if i==temp-1:
                p.append(x)
                x=x+2
for _ in range(t):
    n=int(input())
    print(p[(p[n-1])-1])