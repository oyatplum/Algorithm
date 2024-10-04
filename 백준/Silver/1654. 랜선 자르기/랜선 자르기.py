import sys
input = sys.stdin.readline

N, M = map(int, input().split())

inputList = []

for i in range(N):
    inputList.append(int(input()))

start = 1
maxLen = max(inputList)
result = 0

while start <= maxLen:
    mid = (start + maxLen) // 2
    count = 0

    for i in inputList:
        count += i // mid

    if count >= M:
        start = mid + 1
        result = mid
    else:
        maxLen = mid - 1

print(result)