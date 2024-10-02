import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []
sum = 0

for _ in range(N):
    inputNum = int(input().strip())
    sum += inputNum
    arr.append(inputNum)

arr.sort()

a = Counter(arr).most_common(2)

most = 0
if len(a) > 1:
    if a[0][1] == a[1][1]:
        most = a[1][0]
    else:
        most = a[0][0]
else:
    most = a[0][0]

print(round(sum / N))
print(arr[N//2])
print(most)
print(max(arr) - min(arr))