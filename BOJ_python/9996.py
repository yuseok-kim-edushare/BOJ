#처음 정답 판정 후 약간 수정을 했음
import re
n = int(input())
patterns=input().rstrip().split('*') # rstrip을 굳이 안 써도 굴러가니 생략
le=len(patterns) #처음 정답이후 이 라인 사용 안 함, 변수 길이는 구하고 이용을 안 했음
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