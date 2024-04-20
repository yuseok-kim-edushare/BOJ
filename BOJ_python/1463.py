n=int(input())
counting=[0]*1000001
def trace(i):
    if i<=1:
        pass
    elif counting[i]==0:
        a=(i%2==0)
        b=(i%3==0)
        if a and b:
            counting[i]=1+min(trace(i//3),trace(i//2),trace(i-1))
        elif a:
            counting[i]=1+min(trace(i//2),trace(i-1))
        elif b:
            counting[i]=1+min(trace(i//3),trace(i-1))
        else: counting[i]=1+trace(i-1)
    return counting[i]
if n==1:
    pass
elif counting[n]==0:
    for x in range(n+1):
        trace(x)
else:
    pass
print(counting[n])