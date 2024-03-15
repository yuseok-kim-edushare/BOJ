n = int(input())
def facto(i):
    if i<0:
        pass
    if i<2:
        a= 1
    else:
        a = i * facto(i-1)
    return a
b=facto(n)
b = str(b)
k = len(b) -1
count = 0
while True:
    if b[k]=='0':
        count = count+1
        k = k -1
        continue
    else:
        print(count)
        break