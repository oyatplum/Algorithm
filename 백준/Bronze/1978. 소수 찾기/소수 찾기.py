import sys
input = sys.stdin.readline
count = 0

total = int(input())
numList = list(map(int, input().split()))

for i in numList:
    if i == 1:
        total -= 1
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
            else:
                continue

print(total - count)