def solution(n, lost, reserve):
    answer = 0
    before = [1] * (n+1) #마지막에 인덱스 0 빼주기
    
    for l in lost:
        before[l] = 0
    
    for r in reserve:
        before[r] = 2
        if r in lost: #여분있는 사람이 도난
            before[r] = 1
            
    del before[0]
    
    for idx, b in enumerate(before):
        if idx == 0: #맨 앞인 경우
            if b == 0:
                if before[idx+1] == 2:
                    before[idx+1] = 1
                    before[idx] = 1
            
        elif idx == n-1: #맨 뒤인 경우
            if b == 0:
                if before[idx-1] == 2:
                    before[idx-1] = 1
                    before[idx] = 1
        else:
            if b == 0:
                if before[idx-1] == 2:
                    before[idx-1] = 1
                    before[idx] = 1
                elif before[idx+1] == 2:
                    before[idx+1] = 1
                    before[idx] = 1
    
    for i in before:
        if i >= 1:
            answer += 1
        
    return answer