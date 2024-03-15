n = int(input())
ns=[0]*n
for i in range(0,n):
    ns[i]=int(input())
ns.sort()
for k in range(0,n):
    print(ns[k])