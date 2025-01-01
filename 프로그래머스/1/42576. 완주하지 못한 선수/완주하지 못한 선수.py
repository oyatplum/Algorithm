from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p = Counter(participant)
    c = Counter(completion)
    
    for i in p-c:
        answer = i
        
    return answer