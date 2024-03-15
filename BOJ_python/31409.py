n=int(input())
count=0
phone=list(map(int,input().split()))
for i in range(0,n):
    if phone[i]==i+1:
        count=count+1
        if i==0:
            phone[i]=i+2
        else:
            phone[i]=i
print(count)
for x in range(0,n):
    print(phone[x],end=' ')