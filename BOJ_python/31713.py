import sys
input=sys.stdin.readline #readline 사용시 44ms 미사용시 204 ms
t=int(input())
for i in range(t):
    stem,leaf=map(int,input().split())
    if leaf>=(3*stem) and leaf<=(4*stem):
        print(0)
    else:
        ltest=leaf-(3*stem)
        htest=leaf-(4*stem)
        if ltest<0:
            print(0-ltest)
        tc=0
        while htest>0:
            c=htest//4
            if c==0:
                c=1
            tc=tc+c
            stem=stem+c
            ltest=leaf-(3*stem)
            htest=leaf-(4*stem)
            if ltest<=0:
                print(tc-ltest)
            elif htest<=0:
                print(tc)