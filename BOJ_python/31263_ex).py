n = int(input())
s=input()
count=0
while len(s) > 2:
    if  len(s) == 3 or s[0+3] != "0"  :
        if int(s[0:0+3]) <= 641 :
            s = s[3:]
            count+=1
        else:
            if s[0+2] != "0":
                s = s[2:]
                count+=1
            else:
                s= s[1:]
                count+=1
    elif s[0+2] != "0":
        s = s[2:]
        count+=1
    else:
        s= s[1:]
        count+=1
if len(s)>0:
    count=count+1
print(count)