t=1+int(input())
t=bin(t)
p=t[3:]
a=''
for x in range(0,len(p)):
    if p[x]=='0':
        a=a+'4'
    else:
        a=a+'7'
print(a)