def dfs(start, visited, computers):
    if visited[start] == 0:
        visited[start] = 1
        for i in range(len(computers)):   
            if visited[i] == 0 and computers[start][i] == 1 and i != start:
                dfs(i, visited, computers)
        return 1
    else:
        return 0
    
            
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        returned = dfs(i, visited, computers)
        answer += returned
    return answer