from collections import defaultdict
def dfs(start, graph, visited):
    visited[start] = 1
    count = 1
    for nextNode in graph[start]:
        if visited[nextNode] != 1:
            count += dfs(nextNode, graph, visited)
    return count
    
def solution(n, wires):
    answer = -1
    arr = []
    for i in range(len(wires)):
        copyWires = wires.copy()
        del copyWires[i]
        graph = defaultdict(list)

        for a,b in copyWires:
            graph[a].append(b)
            graph[b].append(a)
        visited = [0] * (n+1)
        
        temp = []
        for i in range(1, n+1):
            returned = dfs(i, graph, visited)
            if returned == 1:
                continue
            else:
                temp.append(returned)
        
        if len(temp) == 1:
            arr.append(temp[0]-1)
        else:
            arr.append(abs(temp[0] - temp[1]))
    return min(arr)