t=int(input())
counts=['']*200
counts[0]='1 0'
counts[1]='0 1'
counts[2]='1 1'
def count_febo(num):
    if counts[num]=='':
        f2=list(map(int,count_febo(num-2).split()))
        f1=list(map(int,count_febo(num-1).split()))
        c0=f2[0]+f1[0]
        c1=f2[1]+f1[1]
        counts[num]=str(c0)+' '+str(c1)
    else:
        pass
    return counts[num]
for x in range(0,t):
    req=int(input())
    ans=count_febo(req)
    print(ans)
