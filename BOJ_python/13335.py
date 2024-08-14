n, bridge_length, can_holding_weight = map(int, input().split())
trucks = list(map(int, input().split()))
bridge=[]
net_weights = 0
answer = 1
while trucks:
    if net_weights + trucks[0] <= can_holding_weight:
        entranceTruck = trucks.pop(0)
        bridge.append([entranceTruck, bridge_length])
        net_weights += entranceTruck
    if bridge:
        answer += 1
        for i in range(len(bridge)):
            bridge[i][1] -= 1
        if bridge[0][1] == 0:
            escapeTruck = bridge.pop(0)
            net_weights -= escapeTruck[0]
print(answer+bridge_length)
        
