n=int(input())
for x in range(0,n):
    data=input()
    p=0
    test=1
    for k in range(0,len(data)):
        if data[k]=='(':
            p=p+1
        elif data[k]==')':
            p=p-1
        if p<0:
            test=0
    if p!=0:
        test=0
    if test==1:
        print('YES')
    else:
        print('NO')