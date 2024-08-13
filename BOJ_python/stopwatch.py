import sys
import time
import subprocess


number = input("어느 소스 실행할거야?")
startTime = time.time()
exec(open(number+".py").read())
print("excution time: %f"%(time.time() - startTime))
