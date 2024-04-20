import sys
input=sys.stdin.readline
n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input().rstrip()))
nums.sort()

print(round((sum(nums)+0.000001)/n))
print(nums[(n-1)//2])

frq=0
numRange=nums[n-1]-nums[0]
frqs=[0]*(numRange+1)
for x in nums:
    temp=x-nums[0]
    frqs[temp]=frqs[temp]+1
mfrq=max(frqs)
all_mfrq_index = sorted(list(filter(lambda x: frqs[x] == mfrq, range(len(frqs)))))
if len(all_mfrq_index)==1:
    frq=all_mfrq_index[0]+nums[0]
else:
    frq=all_mfrq_index[1]+nums[0]
    
print(frq)
print(numRange)
