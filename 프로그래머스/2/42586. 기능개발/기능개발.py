answer = []

def solution(progresses, speeds):
    global answer
    num = 0
    while progresses[0] < 100:
        for i, (j,k) in enumerate(zip(progresses, speeds)):
            progresses[i] = j + k

    for i in progresses[:]:
        if i >= 100:
            progresses.pop(0)
            speeds.pop(0)
            num += 1
        else:
            break
    answer.append(num)

    if len(progresses) == 0:
        return answer
    else:
        return solution(progresses, speeds)