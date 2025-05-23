from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    
    for p in participant:
        dic[p] += 1
    
    for c in completion:
        if dic[c] >= 1:
            dic[c] -= 1
    
    for d in dic:
        if dic[d] == 1:
            return d