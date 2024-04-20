import sys
import collections
from collections import deque
input=sys.stdin.readline
st=deque()
s=True
def prop(a):
    global st
    switch1=False
    for i in a:
        if i=='(':
            st.append(i)
        elif i==')':
            if len(st)==0:
                switch1=True
            else:
                temp=st.pop()
                if temp!='(':
                    switch1=True
        elif i=='[':
            st.append(i)
        elif i==']':
            if len(st)==0:
                switch1=True
            else:
                temp=st.pop()
                if temp!='[':
                    switch1=True
    if len(st)>0:
        switch1=True
        st=deque()
    if switch1:
        print("no")
    else:
        print("yes")
while s:
    a=input()
    if a[0]=='.':
        s=False
        break
    else:
        stat=prop(a)