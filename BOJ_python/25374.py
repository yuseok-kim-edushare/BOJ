n=input()
scores=sorted(list(map(int,input().split())))
gradediv=[96,89,77,60,40,23,11,4,0]
t=1000
b=100
stacked=0
for g in range(0,len(gradediv)):
    b=100-stacked
    s=0
    if b<gradediv[g]:
        print(0)
    else:
        if b==0:
            t=0
        else:
            t=scores.index(scores[gradediv[g]])
        s=b-t
        stacked=stacked+s
        print(s)