n=int(input())
pat='666'
num=['0','1','2','3','4','5','6','7','8','9']
ans=set([])
for a in num:
    for x in num:
        for y in num:
            for z in num:
                for i in range(5):
                    if i==0:
                        t1=''
                        t2=a+x+y+z
                    elif i==1:
                        t1=a
                        t2=x+y+z
                    elif i==2:
                        t1=a+x
                        t2=y+z
                    elif i==3:
                        t1=a+x+y
                        t2=z
                    else:
                        t1=a+x+y+z
                        t2=''
                    temp=t1+pat+t2
                    ans.add(temp)
ans=list(ans)
ans.sort()
print(int(ans[n-1]))