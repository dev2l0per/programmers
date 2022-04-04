from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    
    while bridge:
        answer += 1
        popWeight = bridge.pop(0)
        bridge_weight -= popWeight
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)
    
    return answer