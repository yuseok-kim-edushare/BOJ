docu=input()
pat=input()
l=len(pat)
count=0
i=docu.find(pat)
while i !=-1:
    docu2=docu[i+l:]
    docu=docu2
    count=count+1
    i=docu.find(pat)
print(count)