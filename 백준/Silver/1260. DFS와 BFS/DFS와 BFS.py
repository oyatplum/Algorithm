import sys
input = sys.stdin.readline
from collections import deque

N,M,V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

visitedD = [0]*(N+1)
visitedB = [0]*(N+1)

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def DFS(v):
    visitedD[v] = 1
    print(v, end=" ")
    for i in range(N+1):
        if graph[v][i] == 1 and visitedD[i] == 0:
            DFS(i)
def BFS(v):
    q = deque()
    q.append(v)
    visitedB[v] = 1
    while q:
        p = q.popleft()
        print(p, end=" ")
        for i in range(N+1):
            if graph[p][i] == 1 and visitedB[i] == 0:
                q.append(i)
                visitedB[i] = 1

DFS(V)
print()
BFS(V)
