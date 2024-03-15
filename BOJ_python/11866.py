n,k=map(int,input().split())
temp=list(range(1,n+1))
s='<'
i=-1
while temp!=[]:
    l=len(temp)
    if i+k>=l:
        i=i+k-l
        while i>=l:
            i=i-l
    else:
        i=i+k
    s=s+str(temp[i])+', '
    temp.remove(temp[i])
    i=i-1
s=s[:-2]+'>'
print(s)