def colorMissmatch(a, b):
    if a!=b:
        return 1
    else:
        return 0

n, k = map(int, input().split())
bulbs = list(map(int, input().split()))

abstract_bulbs = []
mem = 0
for x in bulbs:
    if x != mem:
        abstract_bulbs.append(x)
        mem=x

groups = len(abstract_bulbs)
if groups == 1:
    print(0)
else:
    dp = [[99999999]*(groups) for _ in range(groups)]
    
    def solve(left, right):
        if (left >= right):
            return 0
        if (dp[left][right] != 99999999):
            return dp[left][right]
        for mid in range(left, right):
            ll = solve(left, mid)
            rr = solve(mid + 1, right)
            dp[left][right] = min(dp[left][right], ll + rr + colorMissmatch(abstract_bulbs[left], abstract_bulbs[mid+1]))
        return dp[left][right]

    print(solve(0,groups-1))
