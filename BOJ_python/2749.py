n=int(input())
p=1500000 #피사노 주기 15*(num/10)
a=0
b=1
c=1
for x in range(2,1+n%p):
    c=(a+b)%1000000
    a=b
    b=c
print(c)