def solution(priorities, location):
    answer = 0
    while priorities:
        maxN = max(priorities)
        if priorities[0] < maxN: #다시 뒤로
            temp = priorities.pop(0)
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else: #pop
            priorities.pop(0)
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1