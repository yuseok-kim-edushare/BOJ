t=int(input())
for x in range(0,t):
    a,b=map(int,input().split())
    p=a%10
    if p==0:
        print(10)
    elif p==1:
        print(1)
    elif p==2:
        pp=b%4
        d=[6,2,4,8]
        print(d[pp])
    elif p==3:
        pp=b%4
        d=[1,3,9,7]
        print(d[pp])
    elif p==4:
        pp=b%2
        d=[6,4]
        print(d[pp])
    elif p==5:
        print(5)
    elif p==6:
        print(6)
    elif p==7:
        pp=b%4
        d=[1,7,9,3]
        print(d[pp])
    elif p==8:
        pp=b%4
        d=[6,8,4,2]
        print(d[pp])
    elif p==9:
        pp=b%2
        d=[1,9]
        print(d[pp])
