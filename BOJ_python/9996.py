#ó�� ���� ���� �� �ణ ������ ����
import re
n = int(input())
patterns=input().rstrip().split('*') # rstrip�� ���� �� �ᵵ �������� ����
le=len(patterns) #ó�� �������� �� ���� ��� �� ��, ���� ���̴� ���ϰ� �̿��� �� ����
p =patterns[0]+'[a-z]*'+patterns[1]
pp = re.compile(p)
for x in range(0,n):
    name=input()
    if None==re.fullmatch(pp,name):
        print("NE")
    else:
        print("DA")
        
#import re
#n = int(input())
#ps=input().split('*')
#p=ps[0]+'[a-z]*'+ps[1]
#pp=re.compile(p)
#for x in range(0,n):
#    name=input()
#    if None==re.fullmatch(pp,name):
#        print("NE")
#    else:
#       print("DA")