from collections import defaultdict
def solution(clothes):
    dic = defaultdict(list)
    
    for cloth in clothes:
        dic[cloth[1]] += [cloth[0]]
    temp = 1
    for d in dic:
        temp *= len(dic[d]) + 1
        
    return temp - 1