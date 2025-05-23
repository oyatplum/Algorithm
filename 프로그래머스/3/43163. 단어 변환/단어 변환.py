from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = [begin]
    
    if target not in words: #변환할 수 없는 경우    
        return 0
    
    q.append(begin)
    
    while q:
        answer += 1
        for _ in range(len(q)):
            poped = q.popleft()
            for word in words:
                if word not in visited: #중복 제거위해
                    same = 0
                    diff = 0
                    for p, w in zip(poped, word):
                        if p == w:
                            same += 1
                        else:
                            diff += 1
                    if same == len(poped) - 1 and diff == 1:
                        if word == target:
                            return answer
                        visited.append(word)
                        q.append(word)
    
    return answer