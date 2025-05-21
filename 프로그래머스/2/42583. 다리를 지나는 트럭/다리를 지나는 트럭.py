from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    ingTruck = deque()
    totalWeight = 0
    readyTrucks = deque(truck_weights)
    
    while readyTrucks:
        poped = readyTrucks.popleft()
        if len(ingTruck) == bridge_length:
            iPoped = ingTruck.popleft()
            totalWeight -= iPoped
        if totalWeight + poped <= weight and len(ingTruck) < bridge_length:
            ingTruck.append(poped)
            totalWeight += poped
            answer += 1
        else:
            ingTruck.append(0)
            readyTrucks.appendleft(poped)
            answer += 1

    return answer + bridge_length