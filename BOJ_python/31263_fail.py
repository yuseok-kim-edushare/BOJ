n=int(input())
st=input()
temp=['','','']
tidx=0
count=0
switch1=0
def prot(s,idx):
    global st
    global temp
    global tidx
    global count
    global switch1
    temp[tidx]=s
    if tidx==0:
        if s=='0':
            if st[idx-1]=='0':
                temp=['','','']
                count=count+1
            else:
                if st[idx-1] in ['7','8','9']:
                    temp=['','','']
                    count=count+1
                    tidx=0
                else:
                    temp=[st[idx-1],'0','']
                    tidx=2
        elif s in ['7','8','9']:
            switch1=1
            tidx=1
        elif s=='6':
            switch1=2
            tidx=1
        else:
            tidx=1
    elif tidx==1:
        if switch1==1:
            temp=['','','']
            count=count+1
            tidx=0
            switch1=0
        elif switch1==2:
            if s in ['5','6','7','8','9']:
                temp=['','','']
                count=count+1
                tidx=0
                switch1=0
            elif s=='4':
                tidx=2
            else:
                tidx=2
                switch1=0
        else:
            tidx=2
    elif tidx==2:
        if switch1==2:
            if s in ['0','1']:
                temp=['','','']
                count=count+1
                tidx=0
            else:
                temp=[s,'','']
                count=count+1
                tidx=1
            switch1=0
        else:
            temp=['','','']
            count=count+1
            tidx=0
for i in range(0,n):
    prot(st[i],i)
if temp[0]!='':
    count=count+1
print(count)
