from collections import Counter
def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    
    for p in part:
        if p in comp and part[p] == comp[p]:
            continue
        else:
            return p