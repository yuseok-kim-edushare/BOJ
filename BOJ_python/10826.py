n=int(input())
febos=[0]*10005
febos[1]=1
for x in range(2,n+1):
    febos[x]=febos[x-2]+febos[x-1]
ans=febos[n]
print(ans)