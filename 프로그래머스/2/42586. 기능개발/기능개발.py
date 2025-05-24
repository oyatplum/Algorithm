from collections import deque
def check(pro, sp):
    while pro[0] < 100:
        for idx, (p,s) in enumerate(zip(pro, sp)):
            pro[idx] = p + s
    return pro
    
def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    sp = deque(speeds)
    
    while pro:
        returned = check(pro, sp)
        co = returned.copy()
        temp = 0
        
        for i in co:
            if i >= 100:
                pro.popleft()
                sp.popleft()
                temp += 1
            else:
                break
        if temp > 0:
            answer.append(temp)
    
    return answer