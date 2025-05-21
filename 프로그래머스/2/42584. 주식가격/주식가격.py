from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        temp = 0
        poped = q.popleft()
        for p in q:
            if poped <= p:
                temp += 1
            else:
                temp += 1
                break
        answer.append(temp)
    return answer