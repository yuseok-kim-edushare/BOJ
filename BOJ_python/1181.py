import sys
n = int(sys.stdin.readline().rstrip())
inputwords=set()
iwordslen=[]
answer=[]
for x in range(0,n):
    inputwords.add(sys.stdin.readline().rstrip())
inputwords=list(inputwords)
n = len(inputwords)
k = range(0,n)
for t in k:
    iwordslen.append(len(inputwords[t]))
lenrange=list(set(iwordslen))
lenrange.sort()
for j in lenrange:
    idxes=[]
    temp=[]
    for jj in k:
        if iwordslen[jj]==j:
            idxes.append(jj)
    for jjj in range(0,len(idxes)):
        temp.append(inputwords[idxes[jjj]])
    temp.sort()
    answer=answer+temp
for i in k:
    print(answer[i])
