n = int(input())
array = list(map(int, input().split()))
count = 0
if n < 3: pass
else:
    isConvex = False
    while not isConvex:
        isConvex = True
        for i in range(1,n-1):
            if array[i-1] + array[i+1] < 2 * array[i]:
                diff = (array[i-1] + array[i+1]) // 2
                count += (array[i] - diff)
                array[i] = diff
                #array[i-1], array[i] = array[i], array[i-1]
                #count += 1
                isConvex = False
print(count)
