n,m = map(int,input().split())
table=[]
test=[]
for _ in range(n):
    table.append(input())
for i in range(n-7):
    for j in range(m-7):
        count1=0
        count2=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if table[a][b] =='B':
                        count1=count1+1
                    else:
                        count2=count2+1
                else:
                    if table[a][b] =='W':
                        count1=count1+1
                    else:
                        count2=count2+1
        test.append(count1)
        test.append(count2)
print(min(test))
