import sys
readline = sys.stdin.readline

t = int(readline()) # amount of test cases t
for i in range(t):
    job_amount, location = map(int, readline().split()) # amount of jobs and interested job's location
    jobs = list(map(int, readline().split())) # queue of job's priority
    count = 0 # proeceeded job counter
    while location != -1:
        if location == 0:
            if jobs[0] == max(jobs):
                count += 1
                location = -1 #now interested job done
            else:
                jobs.append(jobs.pop(0)) #queue pop and queue push
                location = len(jobs) - 1
        elif jobs[0] == max(jobs):
            jobs.pop(0)
            count += 1
            location -= 1 #trace our interested job is where
        else:
            jobs.append(jobs.pop(0)) #queue pop and queue push
            location -= 1
    print(count)
