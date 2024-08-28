from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

N = int(input())

for i in range(1,N+1):
    queue.append(i)

while True:
    if len(queue) == 1:
        break
    queue.popleft()
    queue.append(queue.popleft())
    continue

print(queue.popleft())