def solution(clothes):
    answer = 1
    dictC = dict()
    for cloth, kind in clothes:
        if kind in dictC.keys():
            dictC[kind] += [cloth]
        else:
            dictC[kind] = [cloth]

    for i in dictC:
        answer *= (len(dictC[i]) + 1)
    return answer - 1

