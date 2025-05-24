from collections import deque
def compare(poped, prices):
    temp = 0
    for i in prices:
            if poped <= i:
                temp += 1
            else:
                temp += 1
                break
    return temp
                
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        poped = prices.popleft()
        returned = compare(poped, prices)
        answer.append(returned)
    
    return answer