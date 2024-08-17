import sys
readline = sys.stdin.readline

n = int(readline()) #how long our array?
answer = [] #this is answer stack
methods = [] #log +(push) and -(pop)
isImpossible = False #boolean flag for impossiblity
#try to make answer by method calling
taskstack = [] #stack for process jobs
#input answer stack
for _ in range(n):
    answer.append(int(readline()))
num = 1
for idx in answer:
    if isImpossible:
        break
    else:
        while not isImpossible:
            if taskstack and taskstack[-1] == num:
                methods.append('-')
                taskstack.pop()
                break
            if num > idx:
                isImpossible = True
            taskstack.append(num)
            methods.append("+")
            num += 1
if isImpossible:
    print("NO")
else:
    print(*methods,sep="\n")
