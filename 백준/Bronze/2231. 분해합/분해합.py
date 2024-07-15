import sys
input = sys.stdin.readline

N = int(input())
min = 0

for i in range(1, N):
    total = i
    for j in str(i):
        total += int(j)
    if total == N:
        min = i
        break

print(min)