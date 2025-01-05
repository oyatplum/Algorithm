def solution(clothes):
    answer = 1
    d = {}
    
    for name, kind in clothes:
        if kind in d.keys():
            d[kind] += [name]
        else:
            d[kind] = [name]
    for kind in d:
        answer *= len(d[kind]) + 1
    return answer - 1