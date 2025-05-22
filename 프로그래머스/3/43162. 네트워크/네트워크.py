def dfs(n, computers, visited, com):
    if visited[com] == 0:
        visited[com] = 1 #방문
        for i in range(n):
            if visited[i] != 1 and computers[com][i] == 1: #연결된 조건
                dfs(n, computers, visited, i)
        return 1
    else:
        return 0
        
            
    
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for com in range(n):
        answer += dfs(n, computers, visited, com)
    return answer