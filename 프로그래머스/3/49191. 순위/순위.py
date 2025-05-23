from collections import defaultdict, deque
def solution(n, results):
    answer = 0
    graphWin = defaultdict(set)
    graphLose = defaultdict(set)
    
    for a, b in results:
        graphWin[a].add(b)
        graphLose[b].add(a)

    def bfs(graph, node):
        q = deque()
        q.append(node)
        visited = [0] * (n+1)
        visited[node] = 1
        
        while q:
            poped = q.popleft()
            for nextNode in graph[poped]:
                if visited[nextNode] == 0:
                    visited[nextNode] = 1
                    q.append(nextNode)
                    graph[node].add(nextNode)
    
    for node in range(1, n+1):
        bfs(graphWin, node)
        bfs(graphLose, node)
    
    print(graphWin)
    print(graphLose)
    
    for i in range(1, n+1):
        winCount = len(graphWin[i])
        loseCount = len(graphLose[i])
        if winCount + loseCount == n-1:
            answer += 1
    
    
                
        
    return answer