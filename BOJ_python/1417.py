import sys
input=sys.stdin.readline
n=int(input())
if n==1:
    input()
    print(0)
else:
    votes=[0]*n
    me=int(input())
    for x in range(1,n):
        votes[x]=int(input())
    rival=max(votes)
    if me-rival>0:
        print(0)
    else:
        count=0
        while rival-me>=0:
            idx=votes.index(rival)
            me=me+1
            count=count+1
            votes[idx]=rival-1
            rival=max(votes)
        print(count)
