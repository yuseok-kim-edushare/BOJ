import sys
n=sys.stdin.readline()
a=set(sys.stdin.readline().rstrip().split())
m=sys.stdin.readline()
b=list(sys.stdin.readline().rstrip().split())
for x in b:
    if x in a:
        print(1)
    else:
        print(0)