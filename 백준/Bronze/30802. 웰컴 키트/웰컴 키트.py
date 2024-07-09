import sys
input = sys.stdin.readline
count = 0

total = int(input())
shirtSizeList = list(map(int, input().split()))
T, P = map(int, input().split())

for i in shirtSizeList:
    if i == 0:
        continue
    elif i <= T:
        count += 1
    else:
        count += (i - 1) // T + 1

print(count)
print(total // P, total % P)