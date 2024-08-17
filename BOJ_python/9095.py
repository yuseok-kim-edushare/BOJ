caselist = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
#for i in range(4,11):
#    caselist.append((caselist[i-1] + caselist[i - 2] + caselist[i -3]))
t = int(input())
for i in range(t):
    number = int(input())
    print(caselist[number])
