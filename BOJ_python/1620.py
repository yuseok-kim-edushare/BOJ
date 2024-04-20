import sys
input=sys.stdin.readline
n,m=map(int,input().split())
Pokedex1=dict()
Pokedex2=['']*(n+1)
for i in range(n):
    t=input().rstrip() #rstrip() 필요한 문제였으..
    Pokedex1[t]=i+1
    Pokedex2[i+1]=t
for k in range(m):
    temp=input().rstrip()
    if temp in Pokedex1:
        print(Pokedex1[temp])
    else:
        print(Pokedex2[int(temp)])