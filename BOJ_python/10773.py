k = int(input())
i = 0
a =[]
while i<k:
    i = i+1
    t=int(input())
    if 0==t:
        a.pop()
    else:
        a.append(t)
print(sum(a))

#Ʋ�ȴ� �ڵ��
#t ����, if 0==input():
#        else: a.append(int(input()))
#�ϴ� �ٶ��� EOFerror