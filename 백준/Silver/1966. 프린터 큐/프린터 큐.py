import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
outputList = []

for _ in range(T):
    queue = deque()
    N, M = map(int, input().split())
    inputList = input().split()

    for i in inputList:
        queue.append(i)

    count = 0

    while True:
        if queue[0] < max(queue):
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
            queue.append(queue.popleft())
            continue
        else:
            if M != 0:
                queue.popleft()
                M -= 1
                count += 1
                continue
            else:
                count += 1
                break
    outputList.append(count)

for i in outputList:
    print(i)