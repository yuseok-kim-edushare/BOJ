scores=0.0
credits=0.0
grades={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for x in range(0,20):
    p=input().split()
    if p[2]!='P':
        credit=float(p[1])
        credits=credits+credit
        scores=scores+credit*grades[p[2]]
avg=scores/credits
print("{0:f}".format(avg))