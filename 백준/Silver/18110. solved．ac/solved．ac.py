import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
average = 0
total = 0
inputList = []
queue = deque()

def roundFunc(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

percent = roundFunc(N*0.15)

if N == 0:
    print(0)
else:
    for _ in range(N):
        inputList.append(int(input()))

    inputList.sort()

    for i in inputList:
        queue.append(i)

    for _ in range(percent):
        queue.popleft()
        queue.pop()

    for i in queue:
        total += i

    average = roundFunc(total / len(queue))
    print(average)