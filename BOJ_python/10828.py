import sys
n = int(input())
i = 0
a=[]
l=0
while i<n:
    i = i+1
    op = sys.stdin.readline().rstrip()
    if op =='size':
        print(l)
    elif op =='empty':
        if 0==l:
            print(1)
        else:
            print(0)
    elif op == 'pop':
        if 0==l:
            print(-1)
        else:
            print(a[l-1])
            a.pop()
            l = l-1
    elif op == 'top':
        if 0==l:
            print(-1)
        else:
            print(a[l-1])
    else:
        op = op[5:]
        t = int(op)
        a.append(t)
        l=l+1