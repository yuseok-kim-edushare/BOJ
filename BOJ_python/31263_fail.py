import collections
from collections import deque
n=int(input())
st=input()
temp=deque()
col=[]
tidx=0
switch1=0
def repair():
    global temp
    global col
def prot(s,idx):
    global st
    global temp
    global tidx
    global col
    global switch1
    temp.append(s)
    if tidx==0:
        if s=='0':
            if st[idx-1]=='0':
                col.append([st[idx-2],'0','0'])
                temp=deque()
            else:
                if st[idx-1] in ['7','8','9']:
                    col.append([st[idx-1],'0',''])
                    temp=deque()
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
            col.append(temp)
            temp=deque()
            tidx=0
            switch1=0
        elif switch1==2:
            if s in ['5','6','7','8','9']:
                col.append(temp)
                temp=deque()
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
                col.append(temp)
                temp=deque()
                tidx=0
                switch1=0
            else:
                temp.pop()
                col.append(temp)
                temp=deque()
                temp.append(s)
                tidx=1
            switch1=0
        else:
            col.append(temp)
            temp=deque()
            tidx=0
for i in range(0,n):
    prot(st[i],i)
if len(temp)!=0:
    col.append(temp)
print(len(col))
