t=int(input().strip())

for k in range(0,t):

    nullline=input()

    n,m= map(int,input().split())

    ciqs=list(map(int,input().split()))

    eiqs=list(map(int,input().split()))

    cav=sum(ciqs)/n

    eav=sum(eiqs)/m

    count=0

    for x in ciqs:

        if x>eav and x<cav:

            count=count+1

    print(count)
