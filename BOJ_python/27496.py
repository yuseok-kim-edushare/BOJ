N, L = map(int,input().split())
a = list(map(int,input().split()))+[0]*N #혹시나 마신 술의 횟수가 대회 때 까지보다 적을 수도 있어서 리스트 끝에 0 보충

tot_alchol = [a[0]]
for i in range(1, N):
    tot_alchol.append(tot_alchol[i-1] + a[i])

now_alchol = tot_alchol[0:L] #처음 마신게 해독 될 때 까진, 각 순간 혈중 알콜은 그 때까지 총 알콜과 같음: 이거 놓쳐서 몇 번 (다른 거 최적화 하고 교정해야 하는 줄 알았음)틀림...
for j in range(N-L):
    now_alchol.append(tot_alchol[j + L] - tot_alchol[j]) 

ans=0
for k in range(len(now_alchol)):
    if now_alchol[k] in range(129,139):
        ans+=1
print(ans)
