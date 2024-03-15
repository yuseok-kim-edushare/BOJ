a=input().split()
a[1]=int(a[1][:-1])
a[2]=int(a[2])
h,m=map(int,a[3].split(':'))
months=dict(January=0, February=31, March=59, April=90, May=120, June=151, July=181, August=212, September=243, October=273, November=304, December=334)
a[0]=months[a[0]]
t= a[2]%4==0 and (not a[2]%100==0 or a[2]%400==0)
stackedmin=m+h*60+(a[1]-1)*1440
yearsmin=0
if t:
    yearsmin=527040
    if a[0]>50:
        a[0]=1+a[0]
else:
    yearsmin=525600
stackedmin = stackedmin + a[0]*24*60
print(100*stackedmin/yearsmin)
