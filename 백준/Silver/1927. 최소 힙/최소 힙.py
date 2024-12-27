import sys
import heapq
input = sys.stdin.readline

heap = []
output = []

N = int(input())

for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(heap) == 0:
            output.append(0)
        else:
            output.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

for i in output:
     print(i)