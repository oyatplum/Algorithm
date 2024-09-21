from collections import deque
import sys
input = sys.stdin.readline

N = (int(input()))
output = []
queue = deque()

for _ in range(N):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            output.append("-1")
        else:
            output.append(queue.popleft())
    elif command[0] == "size":
        output.append(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            output.append("1")
        else:
            output.append("0")
    elif command[0] == "front":
        if len(queue) == 0:
            output.append("-1")
        else:
            output.append(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            output.append("-1")
        else:
            output.append(queue[-1])

for i in output:
    print(i)