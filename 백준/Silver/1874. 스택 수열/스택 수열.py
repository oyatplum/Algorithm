import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
pushNum = 1
isPossible = 1
output = []
N = int(input().strip())

for i in range(N):
    num = int(input().strip())

    while pushNum <= num:
        queue.append(pushNum)
        output.append("+")
        pushNum += 1

    if queue[-1] == num:
        queue.pop()
        output.append("-")
    else:
        isPossible = 0

if isPossible == 1:
    for i in output:
        print(i)
else:
    print("NO")