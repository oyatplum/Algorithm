from collections import deque

queue = deque()
an = []

N, K = map(int, input().split())

for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    an.append(queue.popleft())

print("<", end="")
for i in range(N - 1):
    print(an[i], end=", ")
print(an[N - 1], end="")
print(">")