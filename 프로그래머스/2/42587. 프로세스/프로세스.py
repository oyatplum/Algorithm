from collections import deque

def solution(priorities, location):
    answer = 0
    temp = deque()
    for idx, p in enumerate(priorities): #location 비교 위해
        temp.append([idx, p])
    
    while True:
        maxNum = 0
        for target in temp: # 가장 큰 수 구해놓기
            if maxNum < target[1]:
                maxNum = target[1]
        
        copied = temp.copy()
        
        for target in copied:
            if target[1] < maxNum:
                poped = temp.popleft()
                temp.append(poped)
            else:
                poped = temp.popleft()
                answer += 1
                if poped[0] == location:
                    return answer
                else:
                    break         
    
    return answer