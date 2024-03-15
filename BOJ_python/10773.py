k = int(input())
i = 0
a =[]
while i<k:
    i = i+1
    t=int(input())
    if 0==t:
        a.pop()
    else:
        a.append(t)
print(sum(a))

#틀렸던 코드는
#t 없이, if 0==input():
#        else: a.append(int(input()))
#하는 바람에 EOFerror