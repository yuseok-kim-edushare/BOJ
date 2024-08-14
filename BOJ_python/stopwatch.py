import sys
import time
import subprocess

inputs = []
rights = []


number = input("어느 소스 실행할거야?")
startTime = time.time()
for i in len(inputs):
    answer = solution(inputs[i])
    if answer != rights[i]:
        print("wrong ",i,'\n', rights[i],'\n',answer)
print("excution time: %f"%(time.time() - startTime))
