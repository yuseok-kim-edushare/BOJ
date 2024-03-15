a,b,n=map(int,input().split())
p=0
for x in range(0,n+1):
    if b>a:
        a=a*10
        p=0
    else:
        p=a//b
        a=10*(a%b)
print(p)