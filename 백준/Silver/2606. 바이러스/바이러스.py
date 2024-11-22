import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
visitedD = [0]*(N+1)
visitedB = [0]*(N+1)
count = 0

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def DFS(v):
    visitedD[v] = 1
    global count
    count += 1
    for i in range(N+1):
        if graph[v][i] == 1 and visitedD[i] == 0:
            DFS(i)
DFS(1)

print(count - 1)