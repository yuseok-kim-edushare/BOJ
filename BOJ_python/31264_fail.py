import sys
input=sys.stdin.readline
n,m,a=map(int,input().split())
s=list(map(int,input().split()))
s.sort()
slen=len(s)
rank=s[0]
score=0
shot=0
sidx=0
nrank=rank
while True:
    if s[n-1]<=rank:
        score=s[n-1]*m
        if score>=a:
            break
        else:
            break
    else:
        if score<a:
            if sidx==slen:
                score=score+s[sidx-1]*(m-shot)
                if score>=a:
                    break
                else:
                    rank=rank+1
                    nrank=rank
                    score=0
                    shot=0
                    sidx=0
            elif s[sidx]<=nrank:
                sidx=sidx+1
            else:
                sidx=sidx-1
                score=score+s[sidx]
                nrank=nrank+s[sidx]
                shot=shot+1
                if shot==m:
                    if score<a:
                        rank=rank+1
                        nrank=rank
                        score=0
                        shot=0
                        sidx=0
                    else:
                        break
        else:
            break
print(rank)