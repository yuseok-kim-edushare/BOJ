#�ƿ� ä�� �����ε�, �׳� �̰� Ʋ�Ⱦ�
n=int(input())
cards=list(range(1,n+1))
m=''
for x in range(0,n):
    m=m+str(cards[0])+' '
    cards=cards[1:]
    if x<n-2:
        cards=cards[1:]+[cards[0]]
m=m.rstrip()
print(m)

#�� �ڵ�� ���� ����, �� ����������?
#ans=0
#for x in range(0,n):
#    if len(cards)==1:
#        ans=cards[0]
#    cards=cards[1:]
#    if x<n-2:
#        cards=cards[1:]+[cards[0]]
#print(ans)