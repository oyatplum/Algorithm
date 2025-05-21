def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            poped = answer.pop()
            if poped == i:
                answer.append(poped)
            else:
                answer.append(poped)
                answer.append(i)
    return answer