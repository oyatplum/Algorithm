def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(targetIdx):
        nonlocal visited
        
        for idx, computer in enumerate(computers[targetIdx]):
            if idx != targetIdx and visited[idx] != 1 and computer == 1:
                visited[idx] = 1
                dfs(idx)
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            answer += 1
        else:
            continue
    
    return answer